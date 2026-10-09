import sqlite3

connection = sqlite3.connect("para10_DB.sl3", timeout=5)
cur = connection.cursor()

cur.execute("INSERT INTO first_table (name) VALUES('Lisa');")
cur.execute("INSERT INTO first_table (name) VALUES('Dima');")
cur.execute("INSERT INTO first_table (name) VALUES('Sasha');")

connection.commit()
res = cur.fetchall()
print(res)

connection.close()