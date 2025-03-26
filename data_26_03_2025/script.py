import sqlite3 as sql

#Conectar com o banco de dados
db = sql.connect(/data_26_03_2025/banco.db)

#Criar cursos para exceturar comandos SQL
cursor = db.cursor()

#fazer consulta
cursos.execute("SELECT * FROM cliente;")
resultado = cursor.fetchall()

#Imprimir resultado
for id, nome, email in resultado:
    print(id, nome, email)
