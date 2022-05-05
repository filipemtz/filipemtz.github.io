
import sqlite3

# Initialize connection to the database
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create tables
cur.execute(
    "CREATE TABLE produto(id INTEGER, nome VARCHAR(32), preco REAL, estoque INTEGER)")

cur.execute(
    "CREATE TABLE cliente(cpf VARCHAR(11) UNIQUE, nome VARCHAR(32), email VARCHAR(50))")

# Save (commit) the changes
con.commit()
con.close()
