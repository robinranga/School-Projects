import mysql.connector as c
conn = c.connect(host='localhost',
                database='Practical',
                user='root',
                password='Robin_Ranga')
if conn.is_connected():
    print('....Successfully Connected....')
else:
    print('....An error has occured....')
ch=input('Do you want to print Student Table (Y/N)  ')
if ch in 'nN':
    print('Thanks')
else:
   cur=conn.cursor()
   cur.execute('select * from student')
   data=cur.fetchall()
   for i in data:
       print(i)