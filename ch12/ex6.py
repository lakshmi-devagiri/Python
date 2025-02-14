#(Update  the table example)
#(Giving 1000 bonus to all the employees whose salary is <= 30000)
import mysql.connector
cnx = mysql.connector.connect(user='root', password='oaroar',
                              host='localhost',
                              database='algo')
cur = cnx.cursor()
bonus=int(input("enter the Bonus"))
limit=int(input("enter the limit"))
sql = "update emp set salary = salary+"+str(bonus)+" where salary <="+str(limit)+";"
cur.execute(sql)
cnx.commit()
cnx.close()