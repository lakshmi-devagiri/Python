#(Insert a new record)
import mysql.connector
cnx = mysql.connector.connect(user='root', password='oaroar',
                              host='localhost',
                              database='algo')
cur = cnx.cursor()
sql = "insert into emp values(444,'yyy', 4000)"
cur.execute(sql)
cnx.commit()
cnx.close()