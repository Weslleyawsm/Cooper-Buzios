FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primeiro (cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar resto dos arquivos
COPY . .

# Expor porta
EXPOSE 8001

# Comando para rodar
CMD ["python", "servidor.py"]
