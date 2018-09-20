import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#----------

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
