import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"
mycursor.execute(sql)

#----------

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
