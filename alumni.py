import psycopg2

# Fill in db info
con = psycopg2.connect(database = "ubuntu_server", user = "testuser", password = "test", host = "localhost")
cur = con.cursor()

while True:
   print("Please enter Alumni's First Name:")
   input_fname = str(input())
   cur.execute("SELECT * FROM ALUMNI WHERE Name = %s", (input_fname,))
   print(cur.fetchall())
cur.close()
con.close()
