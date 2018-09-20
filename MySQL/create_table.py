import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#----------

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

#----------

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#----------

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

