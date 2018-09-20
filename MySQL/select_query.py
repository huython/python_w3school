import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#----------

mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#----------

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
