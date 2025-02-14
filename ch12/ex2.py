#(Fetching and printing all the rows of emp table)
import mysql.connector
cnx = mysql.connector.connect(user='root', password='oaroar',
                              host='localhost',
                              database='algo')
cur = cnx.cursor()
cur.execute("select * from emp")
for row in cur.fetchall():
  print(" ",row[0], " ", row[1], " ",row[2]) # coloumn 1, 2, 3 respectively.
cnx.close()