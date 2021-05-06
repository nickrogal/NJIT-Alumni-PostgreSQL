import psycopg2

# Fill in db info
con = psycopg2.connect(database = "ubuntu_server", user = "testuser", password = "test", host = "localhost")
cur = con.cursor()

while True:
   print("Please enter Alumni's First Name:")
   input_name = str(input())
   cur.execute('''SELECT Alumni.Name, Alumni.Email, Alumni.Major, Donations.Donation, Alerts.LastAlert
                    FROM Alumni
                    JOIN Donations 
                    ON Alumni.ID = Donations.AlumniID
                    JOIN Alerts
                    ON Alumni.ID = Alerts.AlumniID
                    WHERE Name = %s''', (input_name,))
   





 #  cur.execute("SELECT * FROM ALUMNI WHERE Name = %s", (input_fname,))
  
  
   print(cur.fetchall())
cur.close()
con.close()
