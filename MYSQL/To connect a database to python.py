import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(host='localhost',
                                       database='ABC',
                                       user='root',
                                       password='robin1234')
cur = conn.cursor()
query = ("select * from ABC")
cur.execute(query)
#cur.fetchall()
#print(cur.fetchall())
for db in cur:
   print(db)


cur.close()
conn.close()
