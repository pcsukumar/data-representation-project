import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
)

cursor = db.cursor()

cursor.execute("create DATABASE employee")

db.close()
cursor.close()