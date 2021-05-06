import psycopg2

# Fill in db info
con = psycopg2.connect(database = "ubuntu_server", user = "testuser", password = "test", host = "localhost")
cur = con.cursor()

while True:
   print("Please enter alumni's first and last name seperated by a space:")
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
        print("Donation Amount: $", row[4])
        print("Donation Date: ", row[5])
   #cur.execute('''SELECT Alumni.Name, Alumni.Email, Alumni.Major, Donations.Donation, Alerts.LastAlert
   #                 FROM Alumni
   #                 JOIN Donations 
   #                 ON Alumni.ID = Donations.AlumniID
   #                 JOIN Alerts
   #                 ON Alumni.ID = Alerts.AlumniID
   #                 WHERE Name = %s''', (input_name,))
   

  
  
   print(cur.fetchall())
cur.close()
con.close()
