import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="huydang",
  passwd="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

#----------

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
