
import sqlite3

# Initialize connection to the database
con = sqlite3.connect('example.db')
cur = con.cursor()

# Insert rows of data
cur.execute(
    "INSERT INTO produto VALUES (1, 'Arroz 5kg', 12.50, 53)")
cur.execute(
    "INSERT INTO produto VALUES (2, 'Oleo', 7.50, 12)")
cur.execute(
    "INSERT INTO produto VALUES (3, 'Pasta de Dente', 4.30, 25)")
cur.execute(
    "INSERT INTO produto VALUES (4, 'Sabonete', 2.75, 123)")
cur.execute(
    "INSERT INTO produto VALUES (5, 'Pizza', 16.50, 3)")
cur.execute(
    "INSERT INTO produto VALUES (6, 'Feijao 2kg', 9.80, 87)")

# Alternative
cur.execute(
    "INSERT INTO cliente(cpf, nome, email) VALUES "
    "('12312312312', 'jose da silva', 'jose@gmail.com'), "
    "('09102931013', 'maria souza', 'maria@gmail.com'), "
    "('63742394181', 'valentina carvalho', 'valentina@hotmail.com'), "
    "('00944732112', 'enzo guilherme moraes', 'enzo.moraes@outlook.com');"
)

# Save (commit) the changes
con.commit()
con.close()
