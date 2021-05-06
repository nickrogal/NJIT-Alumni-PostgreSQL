import psycopg2

# Connect to PostgreSQL DBMS
con = psycopg2.connect(database="ubuntu_server", user='testuser', password='test', host='localhost', port= 5432)
print("Database opened")

cur = con.cursor()

# Adds alumni into alumni table
cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (1, 'First Last', 'x@mail.com', 'Information Technology', Engineering);''')

cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (2, 'Fname Lname', 'y@mail.com', 'Computer Science', Engineering);''')

cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (3, 'Name Name', 'z@mail.com', 'Biology', Biological Sciences);''')

# Adds donations into donations table
cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (1, 1, 50);''')

cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (2, 2, 1000);''')

cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (3, 3, 50000);''')

# Adds alerts into alerts table
cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (1, 1, '2021-5-4 12:30:50');''')

cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (1, 2, '2021-4-47 8:15:00');''')

cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (1, 3, '2021-5-4 1:45:00');''')

con.commit()
con.close()



