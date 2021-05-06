import psycopg2

# Connect to PostgreSQL DBMS
#con = psycopg2.connect(database="postgres", user='postgres', password='password', host='localhost', port= 5432)
con = psycopg2.connect(database="ubuntu_server", user='testuser', password='test', host='localhost', port= 5432)
print("Connected to database successfully!")

con.autocommit = True

# Obtain a DB Cursor
cur = con.cursor()

# Create alumni table
cur.execute('''CREATE TABLE ALUMNI
            (ID INT PRIMARY KEY NOT NULL,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Major TEXT NOT NULL,
            COLLEGE TEXT NOT NULL);''')
print("Alumni table created...")
print("......")

# Create donation table
cur.execute('''CREATE TABLE DONATIONS
            (DonationID INT PRIMARY KEY NOT NULL,
            AlumniID INT NOT NULL,
            Donation MONEY NOT NULL,
            FOREIGN KEY (ALUMNIID) REFERENCES ALUMNI(ID));''')
print("Donations table created...")
print("......")
# Create alerts table

cur.execute('''CREATE TABLE ALERTS
            (AlertID INT PRIMARY KEY NOT NULL,
            AlumniID INT NOT NULL,
            LastAlert TIMESTAMP NOT NULL,
            FOREIGN KEY (ALUMNIID) REFERENCES ALUMNI(ID));''')
print("Alerts table created...")
print("......")
print("All tables created. Party on, Wayne!")

con.commit()
con.close()