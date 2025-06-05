import mysql.connector
from datetime import datetime, time




class DatabaseManager:
    def __init__(self):
        self.config = {
            'host': 'prancheta-db.cgz4mmcgy3ns.us-east-1.rds.amazonaws.com',
            'user': 'admin',
            'password': 'awsm1944',
            'database': 'prancheta_db',
            #'auth_plugin': 'mysql_native_password'
        }
        self.fiscal_atual = None
        self.data_atual = None
        self.linha_atual = None

    def connect(self):
        return mysql.connector.connect(**self.config)

    def cabecalho_prancheta(self, nome_fiscal, data_atual, linha_atual):
        self.fiscal_atual = nome_fiscal
        self.data_atual = data_atual
        self.linha_atual = linha_atual

        print(f"Cabeçalho definido: {self.fiscal_atual} - {self.data_atual} - {self.linha_atual}")

    def inserir_dados_motorista(self, numero_carro, nome_motorista, horario_saida):
        if not self.fiscal_atual or not self.data_atual or not self.linha_atual:
            print(f"Defina todo o cabeçalho antes de prosseguir!")
            return False
        conexao = self.connect()
        cursor = conexao.cursor()

        sql = """INSERT INTO saida_carros
        (nome_fiscal, data_trabalho, linha, numero_carro, nome_motorista, horario_saida)
        VALUES (%s, %s, %s, %s, %s, %s)"""

        valores = (self.fiscal_atual, self.data_atual, self.linha_atual, numero_carro, nome_motorista, horario_saida)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        print(f"Salvo: {numero_carro} - {nome_motorista} - {horario_saida}")
        #return True
        return self.listar_registros()

    def listar_registros(self):
        conexao = self.connect()
        cursor = conexao.cursor()

        sql = """SELECT * FROM saida_carros WHERE nome_fiscal = %s AND data_trabalho = %s AND linha = %s"""
        valores = (self.fiscal_atual, self.data_atual, self.linha_atual)

        cursor.execute(sql, valores)
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()


        print(f"Listando Registro atual!")
        return resultado

    def deletar_registro(self, id_registro):
        conexao = self.connect()
        cursor = conexao.cursor()

        sql = """SELECT * FROM saida_carros WHERE id = (%s)"""
        cursor.execute(sql, (id_registro,))
        registro = cursor.fetchone()
        if not registro:
            print(f"Registro com o ID {id_registro} não encontrado!")
            cursor.close()
            conexao.close()
            return False

        sql = """DELETE FROM saida_carros WHERE id = %s"""
        valores = (id_registro)

        cursor.execute(sql, (valores,))
        conexao.commit()

        cursor.close()
        conexao.close()
        print(f"Registro com id: {id_registro} deletado!")
        return True

        print(f"Registro deletado com sucesso!")

    def listar_todos_registros(self):
        """Lista TODOS os registros sem filtro"""
        conexao = self.connect()
        cursor = conexao.cursor()

        sql = "SELECT * FROM saida_carros ORDER BY id DESC"  # Mais recentes primeiro
        cursor.execute(sql)
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        print(f"Listando TODOS os registros! Total: {len(resultado)}")
        return resultado

    def listar_registros_sessao_atual(self):
        """Lista apenas registros da sessão atual (com cabeçalho definido)"""
        if not self.fiscal_atual or not self.data_atual or not self.linha_atual:
            print("❌ Cabeçalho não definido!")
            return []

        conexao = self.connect()
        cursor = conexao.cursor()

        sql = """SELECT * FROM saida_carros 
                 WHERE nome_fiscal = %s AND data_trabalho = %s AND linha = %s"""
        valores = (self.fiscal_atual, self.data_atual, self.linha_atual)

        cursor.execute(sql, valores)
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()

        print(f"Listando registros da sessão atual! Total: {len(resultado)}")
        return resultado

    '''def debug_completo(self):
        """Função para debugar completamente o banco"""
        print("🔍 === DEBUG COMPLETO ===")

        try:
            conexao = self.connect()
            cursor = conexao.cursor()

            # Teste 1: Verificar se consegue conectar
            print("✅ Conexão estabelecida")

            # Teste 2: Verificar se a tabela existe
            cursor.execute("SHOW TABLES")
            tabelas = cursor.fetchall()
            print(f"📋 Tabelas no banco: {tabelas}")

            # Teste 3: Verificar estrutura da tabela
            cursor.execute("DESCRIBE saida_carros")
            estrutura = cursor.fetchall()
            print(f"🏗️ Estrutura da tabela: {estrutura}")

            # Teste 4: Contar registros
            cursor.execute("SELECT COUNT(*) FROM saida_carros")
            total = cursor.fetchone()[0]
            print(f"📊 Total de registros: {total}")

            # Teste 5: Pegar alguns registros
            cursor.execute("SELECT * FROM saida_carros LIMIT 3")
            alguns = cursor.fetchall()
            print(f"📝 Primeiros registros: {alguns}")

            # Teste 6: Verificar valores NULL
            cursor.execute("SELECT COUNT(*) FROM saida_carros WHERE nome_fiscal IS NULL")
            nulos = cursor.fetchone()[0]
            print(f"❓ Registros com fiscal NULL: {nulos}")

            cursor.close()
            conexao.close()

        except Exception as e:
            print(f"❌ ERRO no debug: {e}")
            print(f"Tipo do erro: {type(e)}")'''
if __name__ == '__main__':
    db = DatabaseManager()
    try:
        conexao = db.connect()
        print("Conexão criada com sucesso!")
        conexao.close()
    except Exception as e:
        print(f"Erro na conexão: {e}")
