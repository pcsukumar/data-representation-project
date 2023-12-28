#To create a table in the database 
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="employee"
)

cursor = db.cursor()
sql="CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), position VARCHAR(250), age INT)"

cursor.execute(sql)

db.close()
cursor.close()