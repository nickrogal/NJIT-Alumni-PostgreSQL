#this script creates the PostgreSQL database and tables


import psycopg2


 

# Connect to PostgreSQL DBMS

con = psycopg2.connect("user=test password='test'");


 

# Obtain a DB Cursor
cursor = con.cursor();

name_Database = "SocialMedia";

 

# Create table statement

sqlCreateDatabase = "create database "+name_Database+";"

 

# Create a table in PostgreSQL database

cursor.execute(sqlCreateDatabase);