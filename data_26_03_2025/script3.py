import sqlite3 as sql

#Conectar com o banco de dados
db = sql.connect('banco.db')

#Criar cursos para exceturar comandos SQL
cursor = db.cursor()

query = """
    insert into cliente (nome, email)
    values (?, ?);
    """

# fazer consulta
import sqlite3 as sql

# Conectar com o banco de dados
db = sql.connect('banco.db')

# Criar cursor para executar comandos SQL
cursor = db.cursor()

# Definir valores para nome e email
nome = "João Silva"
email = "joao.silva@email.com"

# Query para inserir dados
query = """
    insert into cliente (nome, email)
    values (?, ?);
    """

# Executar a consulta
cursor.execute(query, (nome, email))

# Atualizar o banco de dados
db.commit()

# Fechar a conexão com o banco de dados
db.close()
cursor.execute(query, (nome, email))

#atualizar o banco de dados
db.commit()
#fazer consulta de banco de dados
db.close()


