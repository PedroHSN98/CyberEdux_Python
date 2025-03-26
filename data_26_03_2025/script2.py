import sqlite3 as sql

#Conectar com o banco de dados
db = sql.connect('banco.db')

#Criar cursos para exceturar comandos SQL
cursor = db.cursor()

# fazer consulta
cursor.execute(
    """
    insert into cliente (nome, email)
    values ('Guilherme', 'guilherme@gmail.com');
    """
)

#atualizar o banco de dados
db.commit()
#fazer consulta de banco de dados
db.close()


