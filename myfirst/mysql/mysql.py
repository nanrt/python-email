import pymysql

db=pymysql.connect("localhost","root","123456","test")

cursor=db.cursor()

cursor.execute("select * from student")

data=cursor.fetchall()
for i in data:
 print(i)

db.close()