import psycopg2

# Connect to PostgreSQL DBMS
#con = psycopg2.connect(database="postgres", user='postgres', password='password', host='localhost', port= 5432)
con = psycopg2.connect(database="ubuntu_server", user='testuser', password='test', host='localhost', port= 5432)
print("Database opened")

con.autocommit = True

# Obtain a DB Cursor
cur = con.cursor()

# Creates database
#cur.execute("CREATE database ubuntu-server")

# Create alumni table
cur.execute('''CREATE TABLE ALUMNI
            (ID INT PRIMARY KEY NOT NULL,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Major TEXT NOT NULL,
            COLLEGE TEXT NOT NULL);''')

# Create donation table
cur.execute('''CREATE TABLE DONATIONS
            (DonationID INT PRIMARY KEY NOT NULL,
            AlumniID INT NOT NULL,
            Donation REAL NOT NULL,
            FOREIGN KEY (ALUMNIID) REFERENCES ALUMNI(ID));''')

# Create alerts table
cur.execute('''CREATE TABLE ALERTS
            (AlertID INT PRIMARY KEY NOT NULL,
            AlumniID INT NOT NULL,
            LastAlert TIMESTAMP NOT NULL,
            FOREIGN KEY (ALUMNIID) REFERENCES ALUMNI(ID));''')


con.commit()
con.close()