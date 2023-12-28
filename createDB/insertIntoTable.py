#Insert data into employee table

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="employee"
)

cursor = db.cursor()
sql="insert into employee (name, position, age) values (%s,%s, %s)"
values = ("Sara", "Assistant", 35)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()