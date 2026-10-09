import sqlite3

connection = sqlite3.connect("para10_DB.sl3", timeout=5)
cur = connection.cursor()

# cur.execute("CREATE TABLE second_table (pet TEXT);")
# cur.execute("INSERT INTO second_table (pet) VALUES('Cat');")
# cur.execute("INSERT INTO second_table (pet) VALUES('Dog');")
cur.execute("SELECT rowid, pet FROM second_table;")
connection.commit()
res = cur.fetchall()
print(res)

connection.close()