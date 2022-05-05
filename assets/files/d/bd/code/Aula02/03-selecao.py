import pandas as pd
import sqlite3

# Initialize connection to the database
con = sqlite3.connect('example.db')
cur = con.cursor()

# Listar todos os produtos
print("Produtos:")
result = cur.execute("SELECT * FROM produto")
for row in result:
    print(row)

# Listar todos os clientes usando formatacao de strings:
print("\nClientes:")
result = cur.execute("SELECT * FROM cliente")
for row in result:
    print(f'cpf: {row[0]:13} nome: {row[1]:32} email: {row[2]:32}')

# Listar todos os clientes usando formatacao de strings:
print("\nClientes:")
result = cur.execute("SELECT * FROM cliente")
for row in result:
    print(f'cpf: {row[0]:13} nome: {row[1]:32} email: {row[2]:32}')


con.close()
