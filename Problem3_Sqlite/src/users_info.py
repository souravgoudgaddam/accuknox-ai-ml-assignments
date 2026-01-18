import sqlite3
import numpy as np
import pandas as pd

#read data from netflix_users
users=pd.read_csv('Data/netflix_users.csv')
print(users.head(10))

#create connection and database
connection=sqlite3.connect('Data/netflix_users.db')

#create cursor to excute query
cursor=connection.cursor()

#create table users
cursor.execute(""" CREATE TABLE IF NOT EXISTS USERS(
               USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT,
               AGE INTEGER,
               COUNTRY TEXT,
               SUBSCRIPTION_TYPE TEXT,
               WATCH_TIME_HOURS FLOAT,
               FAVOURITE_GENRE TEXT,
               LAST_LOGIN DATE)
""")

connection.commit()




#insert data into database
for index,row in users.iterrows():

    cursor.execute("INSERT INTO USERS(NAME ,AGE,COUNTRY,SUBSCRIPTION_TYPE, WATCH_TIME_HOURS,FAVOURITE_GENRE, LAST_LOGIN)" \
    "VALUES(?,?,?,?,?,?,?)",(
        row['Name'],
        row['Age'],
        row['Country'],
        row['Subscription_Type'],
        row['Watch_Time_Hours'],
        row['Favorite_Genre'],
        row['Last_Login']
    ))
connection.commit()


#retrieve data from table
cursor.execute('select * from users limit 10')

for record in cursor.fetchall():
    print(record)

connection.close()


