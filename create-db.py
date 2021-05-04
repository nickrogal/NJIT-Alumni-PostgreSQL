#create database and tables

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='dbuser',
    password='secureLOL'
)

mycursor = mydb.cursor()

mycursor.execute ("CREATE DATABASE alumni-db")
print("Created database 'alumni-db'")