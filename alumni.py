import psycopg2

# Fill in db info
con = psycopg2.connect(database = "ubuntu_server", user = "testuser", password = "test", host = "localhost")
cur = con.cursor()

while True:
   print("Please enter Alumni's First Name:")
   input_fname = str(input())
   cur.execute("SELECT * FROM ALUMNI WHERE Name = %s", (input_fname,))
   
   
   # print("Getting all alumni...")
    #cur.execute("SELECT * FROM ALUMNI")
    rows = cur.fetchall()

    for row in rows:
        print("ID: ", row[0])
        print("name: ", row[1])
        print("email: ", row[2])
        print("major: ", row[3])
        print("college: ", row[4])

cur.close()
con.close()
