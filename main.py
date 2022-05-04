# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import matplotlib.pyplot as plt
import requests
import pandas as pd
import sqlite3
from pandasgui import show

# JSON
url = requests.get("https://math.uni-pannon.hu/~lipovitsa/szf/zh2022_sz10/bestsellers_with_categories_2022_03_27.json")
text = url.text
dictionary = json.loads(text)

# JSON -> DataFrame -> SQL sync
df = pd.DataFrame(dictionary)

conn = sqlite3.connect('new_db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS books (bookName text, author text, rating text, reviews text, price text, releaseYear text, genre text)')
conn.commit()
df.to_sql('books', conn, if_exists='replace', index= False)

# SQL ellenorzes
# for row in c.fetchall():
#     print(row)

# GUI - a plotting kulon
gui = show(df)

# plottng - nem mindegyik kombinacio mukodik
while True:
    print("X tengely - User Rating/Price/Year ")
    axisX = input()
    print("Y tengely - User Rating/Price/Year ")
    axisY = input()

    plt.bar(df[axisX], df[axisY])
    plt.show()
    print("Ujra? (y/n) ")
    exit = input()
    if exit == "n":
        break








#"Name": "Act Like a Lady, Think Like a Man: What Men Really Think About Love, Relationships, Intimacy, and Commitment",
#    "Author": "Steve Harvey",
#    "User Rating": 4.6,
#    "Reviews": 5013,
#    "Price": 17,
#    "Year": 2009,
#    "Genre": "Non Fiction"
#  },