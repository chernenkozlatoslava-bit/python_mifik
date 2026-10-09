import sqlite3

connection = sqlite3.connect("para10_DB.sl3", timeout=5)
cur = connection.cursor()

cur.execute("CREATE TABLE first_table (name TEXT);")
connection.commit()

connection.close()
