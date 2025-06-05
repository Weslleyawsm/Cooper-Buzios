import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json
from database import DatabaseManager
import os

class MeuServidor(http.server.BaseHTTPRequestHandler):
    # Instância GLOBAL do DatabaseManager (compartilhada)
    db_global = DatabaseManager()

    def __init__(self, *args, **kwargs):
        # Usar a instância global em vez de criar nova
        self.db = MeuServidor.db_global
        super().__init__(*args, **kwargs)

    def enviar_cabecalhos_cors(self):
        """Adiciona cabeçalhos CORS para permitir requisições do frontend"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Responde a requisições OPTIONS (necessário para CORS)"""
        self.send_response(200)
        self.enviar_cabecalhos_cors()
        self.end_headers()

    # MODIFIQUE a função enviar_json para incluir CORS:
    def enviar_json(self, dados):
        """Envia resposta em JSON"""
        resposta = json.dumps(dados, ensure_ascii=False)

        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.enviar_cabecalhos_cors()  # ← ADICIONE ESTA LINHA
        self.end_headers()
        self.wfile.write(resposta.encode('utf-8'))

    # MODIFIQUE também a função enviar_lista_carros:

    def do_GET(self):
        """Responde a requisições GET (páginas, dados)"""
        caminho = self.path

        if caminho == '/' or caminho == '/index.html':
            # Página inicial
            self.servir_arquivo_html()  # ← Use direto, sem redirecionamento
        elif caminho == '/listar':
            # Retorna dados em JSON
            self.enviar_lista_carros()
        else:
            # Página não encontrada
            self.enviar_erro_404()

    def do_POST(self):
        """Responde a requisições POST (formulários)"""
        caminho = self.path

        tamanho = int(self.headers['Content-Length'])
        dados = self.rfile.read(tamanho).decode('utf-8')

        if caminho == '/cabecalho':
            self.processar_cabecalho(dados)
        elif caminho == '/adicionar':
            self.processar_adicionar_carro(dados)
        elif caminho == '/remover':  # ← ADICIONE ESTA LINHA
            self.processar_remover_carro(dados)  # ← E ESTA
        else:
            self.enviar_erro_404()

    def enviar_pagina_inicial(self):
        """Redireciona para o arquivo HTML"""
        # Em vez de retornar HTML, redireciona para o arquivo
        self.send_response(302)
        self.send_header('Location', '/index.html')
        self.end_headers()

    def servir_arquivo_html(self):
        """Serve o arquivo HTML estático"""
        try:
            with open('index.html', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(conteudo.encode('utf-8'))
        except FileNotFoundError:
            self.send_error(404, "Arquivo index.html não encontrado")

    def enviar_lista_carros(self):
        """Envia lista de carros REAL do banco de dados"""
        print("🔍 DEBUG: Função enviar_lista_carros() chamada")

        try:
            print("🔍 DEBUG: Tentando conectar com banco...")

            # Buscar dados reais do banco - TODOS os registros
            registros = self.db.listar_todos_registros()
            print(f"🔍 DEBUG: Registros encontrados: {len(registros)}")
            print(f"🔍 DEBUG: Primeiros registros: {registros[:2] if registros else 'Nenhum'}")

            if len(registros) == 0:
                print("❌ PROBLEMA: listar_todos_registros() retornou vazio!")
                print("🔧 Testando função diretamente...")
                # Teste direto
                teste = self.db.listar_todos_registros()
                print(f"🔧 Teste direto retornou: {len(teste)} registros")

            # Converter para formato JSON amigável
            carros = []
            for registro in registros:
                print(f"🔍 DEBUG: Processando registro: {registro}")

                # Converter tipos MySQL para strings
                data_trabalho = registro[2].strftime('%Y-%m-%d') if registro[2] else None
                horario_saida = str(registro[6]) if registro[6] else None

                carro = {
                    "id": registro[0],
                    "fiscal": registro[1],
                    "data": data_trabalho,
                    "linha": registro[3],
                    "numero": registro[4],
                    "motorista": registro[5],
                    "horario": horario_saida
                }
                carros.append(carro)

            dados = {
                "status": "ok",
                "total": len(carros),
                "carros": carros
            }

            print(f"🔍 DEBUG: Dados finais: {dados}")

        except Exception as e:
            # Se der erro no banco
            print(f"🔍 DEBUG: ERRO capturado: {str(e)}")
            print(f"🔍 DEBUG: Tipo do erro: {type(e)}")

            dados = {
                "status": "erro",
                "mensagem": f"Erro ao buscar dados: {str(e)}",
                "carros": []
            }

        resposta = json.dumps(dados, ensure_ascii=False)

        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.enviar_cabecalhos_cors()  # ← ADICIONE ESTA LINHA
        self.end_headers()
        self.wfile.write(resposta.encode('utf-8'))

    def processar_remover_carro(self, dados):
        """Remove um carro do banco"""
        try:
            # Converter dados do formulário
            parametros = parse_qs(dados)
            id_carro = parametros.get('id', [''])[0]

            print(f"🗑️ Removendo carro ID: {id_carro}")

            # Remover do banco
            sucesso = self.db.deletar_registro(id_carro)

            if sucesso:
                resposta = {
                    "status": "ok",
                    "mensagem": "Carro removido com sucesso!"
                }
            else:
                resposta = {
                    "status": "erro",
                    "mensagem": "Carro não encontrado!"
                }

        except Exception as e:
            print(f"❌ ERRO ao remover carro: {str(e)}")
            resposta = {
                "status": "erro",
                "mensagem": f"Erro ao remover carro: {str(e)}"
            }

        self.enviar_json(resposta)

    def processar_cabecalho(self, dados):
        """Processa dados do cabeçalho REAL"""
        try:
            # Converter dados do formulário para dicionário
            parametros = parse_qs(dados)

            # Extrair valores (parse_qs retorna listas)
            fiscal = parametros.get('fiscal', [''])[0]
            data = parametros.get('data', [''])[0]
            linha = parametros.get('linha', [''])[0]

            print(f"📋 Cabeçalho recebido: Fiscal={fiscal}, Data={data}, Linha={linha}")

            # Salvar no banco através do DatabaseManager
            self.db.cabecalho_prancheta(fiscal, data, linha)

            resposta = {
                "status": "ok",
                "mensagem": "Cabeçalho definido com sucesso!",
                "dados": {"fiscal": fiscal, "data": data, "linha": linha}
            }

        except Exception as e:
            resposta = {
                "status": "erro",
                "mensagem": f"Erro ao salvar cabeçalho: {str(e)}"
            }

        self.enviar_json(resposta)

    def processar_adicionar_carro(self, dados):
        try:
            parametros = parse_qs(dados)
            numero = parametros.get('numero', [''])[0]
            motorista = parametros.get('motorista', [''])[0]
            horario = parametros.get('horario', [''])[0]

            print(f"🚗 Carro recebido: Número={numero}, Motorista={motorista}, Horário={horario}")

            # Salvar no banco
            resultado = self.db.inserir_dados_motorista(numero, motorista, horario)

            if resultado is False:
                # Cabeçalho não foi definido
                resposta = {
                    "status": "erro",
                    "mensagem": "Defina o cabeçalho antes de adicionar carros!"
                }
            else:
                resposta = {
                    "status": "ok",
                    "mensagem": "Carro adicionado com sucesso!",
                    "dados": {"numero": numero, "motorista": motorista, "horario": horario}
                }

        except Exception as e:
            print(f"❌ ERRO ao adicionar carro: {str(e)}")
            resposta = {
                "status": "erro",
                "mensagem": f"Erro ao adicionar carro: {str(e)}"
            }

        self.enviar_json(resposta)



    def enviar_erro_404(self):
        """Página não encontrada"""
        self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1>404 - Pagina nao encontrada</h1>")


if __name__ == '__main__':


    PORT = int(os.environ.get('PORT', 8001))

    with socketserver.TCPServer(("0.0.0.0", PORT), MeuServidor) as httpd:
        print(f"🌐 Servidor rodando em http://localhost:{PORT}")
        print("🔥 Aperte Ctrl+C para parar")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Servidor parado!")