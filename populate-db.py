import psycopg2

# Connect to PostgreSQL DBMS
con = psycopg2.connect(database="ubuntu_server", user='testuser', password='test', host='localhost', port= 5432)
print("Database opened")

cur = con.cursor()

# Adds alumni into alumni table
cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (420, 'Cheech Chong', 'cc420@njit.edu', 'Computer Science', 'Ying Wu College of Computing');''')

cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (69, 'Human Person', 'hh69@njit.edu', 'Information Technology', 'Ying Wu College of Computing');''')

cur.execute('''INSERT INTO ALUMNI (ID, Name, Email , Major , College)
      VALUES (86, 'Tony Soprano', 'ts86@njit.edu', 'Environmental Services and Waste Management', 'Newark College of Engineering');''')

# Adds donations into donations table
cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (1, 420, 420.69);''')

cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (2, 69, 1000.00);''')

cur.execute('''INSERT INTO DONATIONS (DonationID, AlumniID, Donation)
      VALUES (3, 86, 50000.00);''')

# Adds alerts into alerts table
cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (1, 420, '2021-5-4 12:30:50');''')

cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (2, 69, '2021-7-4 8:15:00');''')

cur.execute('''INSERT INTO ALERTS (AlertID, AlumniID, LastAlert)
      VALUES (3, 86, '2021-5-4 1:45:00');''')

con.commit()
con.close()



