import csv
import mysql.connector
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter os dados sensíveis do .env
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

# Conectar ao banco de dados usando os dados do .env
conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Sensor")

# Abrir um arquivo CSV para gravação (com barras duplas no caminho)
with open(r'C:\Users\Thiago\Área de Trabalho\Sensor.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Escrever os nomes das colunas (opcional)
    colunas = [i[0] for i in cursor.description]
    writer.writerow(colunas)

    # Escrever os dados da tabela
    for row in cursor:
        writer.writerow(row)

# Fechar conexões
cursor.close()
conexao.close()

print("Arquivo CSV criado com sucesso!")
