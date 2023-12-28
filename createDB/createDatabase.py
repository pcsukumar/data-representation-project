#To create a database named employee
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  )

cursor = db.cursor()

cursor.execute("create DATABASE employee")

db.close()
cursor.close()