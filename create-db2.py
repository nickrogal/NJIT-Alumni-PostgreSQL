import psycopg2

# Connect to PostgreSQL DBMS
con = psycopg2.connect(database = "ubuntu-server", user = "testuser", password = "testpass", host = "localhost")
print("Database opened")


# Obtain a DB Cursor
cursor = con.cursor()

# Create alumni table
cur.execute('''CREATE TABLE ALUMNI
            (ID INT PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
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
            LastAlert DATETIME NOT NULL,
            FOREIGN KEY (ALUMNIID) REFERENCES ALUMNI(ID));''')


conn.commit()
conn.close()