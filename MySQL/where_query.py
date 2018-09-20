import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#----------

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#----------

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
