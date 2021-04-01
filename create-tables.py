import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  password="secureLOL",
  database="alumni-db"
)

mycursor = mydb.cursor()

#below is a placeholder, need to change and figure out best way to script to create multiple tables
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")