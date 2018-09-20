import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#----------

sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
