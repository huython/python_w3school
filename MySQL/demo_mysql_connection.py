import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678"
)

print(mydb)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#----------

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)
