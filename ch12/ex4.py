#(More generic code to add a new record.)
import mysql.connector
cnx = mysql.connector.connect(user='root', password='oaroar',
                              host='localhost',
                              database='algo')
cur = cnx.cursor()
id = int(input("Enter id: "))
name = input("Enter name: ")
salary = float(input("Enter salary: "))
sql = "insert into emp values ("+ str(id) + "," + "'"+name + "'," + str(salary) + ");"
cur.execute(sql)
cnx.commit()
cnx.close()