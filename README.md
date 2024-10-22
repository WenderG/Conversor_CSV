# Exportar Dados do MySQL para CSV

Este projeto tem como objetivo exportar dados de uma tabela MySQL para um arquivo CSV. O código está escrito em Python e usa a biblioteca `mysql.connector` 
para interagir com o banco de dados e a `csv` para a criação do arquivo CSV. Além disso, utiliza a biblioteca `python-dotenv` para gerenciar de forma segura 
as credenciais de conexão com o banco de dados.

## Funcionalidades

- Conecta-se a um banco de dados MySQL.
- Realiza uma consulta SQL para recuperar os dados de uma tabela.
- Exporta os dados recuperados para um arquivo CSV.
- As credenciais do banco de dados são gerenciadas via um arquivo `.env` para maior segurança.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o seguinte instalado:

- Python 3.x
- MySQL Server
- Pip para instalar as dependências do Python
