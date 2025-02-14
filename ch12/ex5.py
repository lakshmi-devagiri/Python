#(Update  the table example)
#(Giving 1000 bonus to all the employees whose salary is <= 30000)
import mysql.connector
cnx = mysql.connector.connect(user='root', password='oaroar',
                              host='localhost',
                              database='algo')
cur = cnx.cursor()
sql = "update emp set salary = salary+500 where salary <= 3000"
cur.execute(sql)
cnx.commit()
cnx.close()