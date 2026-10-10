import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://chernigov.2ua.org/en/weather/7_days/"

response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")

# connect to Data Base
connection = sqlite3.connect("dz10_DB.sl3", timeout=5)
cur = connection.cursor()

cur.execute("DROP TABLE IF EXISTS weather;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        date TEXT,
        max_temp INTEGER
    );
""")

days = soup.find_all("div", {"class": "wth_ln"})

for elem in days:
    # data with class rd
    date = elem.find("p", {"class": "rd"}) # class_="rd" {"class": "sc-664711f9-0 kXPUOA"}

    # data without class
    if date is None:
        date = elem.find("p", {"class": None})

    # max temperature
    temp = elem.find("p", {"class": "tmp_day"})

    if date is not None and temp is not None:
        date_text = date.text.strip().split()[1] #delete Mon, Tue, Wed...
        #max_temp = temp.text.strip()
        max_temp = int(temp.text.strip().replace("°", "").replace("+", ""))
        # print(date_text, max_temp) #date_text max_temp
        cur.execute(
            "INSERT INTO weather (date, max_temp) VALUES (?, ?)",
            (date_text, max_temp)
        )
connection.commit()

cur.execute("SELECT * FROM weather;")
connection.commit()

res = cur.fetchall()
print(res)

connection.close()