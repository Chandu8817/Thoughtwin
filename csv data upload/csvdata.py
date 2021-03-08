import mysql.connector
import csv


mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="mydatabase"
)


mycursor=mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'), 
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# val = ("Michelle", "Blue Village")
# mycursor.executemany(sql, val)
# mycursor.execute(sql, val)


# mycursor.execute("SELECT name FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.",mycursor.lastrowid)
# mycursor.execute("CREATE DATABASE  mydatabase")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# print(mydb)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

mycursor.execute("CREATE TABLE  emp_detail (name VARCHAR(255),dob DATE doj DATE,email VARCHAR(100), mobile INT(20))")


