#this is the actual alumni application which prompts the user for the alumni's full name seperated by a space and produces the name, email, major, njit college, donation ammount
#and donation date. 
# 
# ctrl+c to quit.

import psycopg2

# connect to the database and set the cursor
con = psycopg2.connect(database = "ubuntu_server", user = "testuser", password = "test", host = "localhost")
cur = con.cursor()

#prompt the user for alumni's name and produce the output
while True:
   print("/nPlease enter alumni's first and last name seperated by a space:")
   input_name = str(input())
   cur.execute('''SELECT ALUMNI.Name, ALUMNI.Email, ALUMNI.Major, ALUMNI.College, DONATIONS.Donation, ALERTS.LastAlert
                    FROM ALUMNI
                    JOIN DONATIONS 
                    ON ALUMNI.ID = DONATIONS.AlumniID
                    JOIN ALERTS
                    ON ALUMNI.ID = ALERTS.AlumniID
                    WHERE Name = %s''', (input_name,))
                    
   rows = cur.fetchall()

   for row in rows:
        print("Alumni Name: ", row[0])
        print("Alumni Email: ", row[1])
        print("Alumni Major: ", row[2])
        print("Alumni NJIT College: ", row[3])
        print("Donation Amount: ", row[4])
        print("Donation Date: ", row[5])

cur.close()
con.close()
