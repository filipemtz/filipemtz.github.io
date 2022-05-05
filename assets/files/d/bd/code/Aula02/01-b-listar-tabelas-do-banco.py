import pandas as pd
from pprint import pprint
import sqlite3

# Initialize connection to the database
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create tables
result = cur.execute(
    "SELECT name, sql FROM sqlite_schema WHERE type = 'table'")

pprint(result.fetchall())

# Alternative
table = pd.read_sql_query(
    "SELECT name, sql FROM sqlite_schema WHERE type = 'table'", con)

print(table.head())

# Save (commit) the changes
con.commit()
con.close()
