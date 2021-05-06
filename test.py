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
            (_id INT PRIMARY KEY NOT NULL,
            f_name TEXT NOT NULL,
            l_name TEXT NOT NULL,
            email TEXT NOT NULL,
            njit_major TEXT NOT NULL,
            njit_college TEXT NOT NULL);''')

# Create donation table
cur.execute('''CREATE TABLE DONATIONS
            (donation_id INT PRIMARY KEY NOT NULL,
            alumni_id INT NOT NULL,
            donation_amount REAL NOT NULL,
            FOREIGN KEY (alumni_id) REFERENCES ALUMNI(_id));''')

# Create alerts table
cur.execute('''CREATE TABLE ALERTS
            (donation_alert_id INT PRIMARY KEY NOT NULL,
            alumni_id INT NOT NULL,
            last_dontation_date TIMESTAMP NOT NULL,
            FOREIGN KEY (alumni_id) REFERENCES ALUMNI(_id));''')


con.commit()
con.close()