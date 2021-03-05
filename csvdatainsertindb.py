
import csv
import mysql.connector


mydb= mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="demodata"
)

# insertdata=mydb.cursor()

# insertdata.executemany

with open("demodata.csv", mode="r") as csv_file:

    csv_read=csv.reader(csv_file)

    line_count=0

    # for x in csv_read:
    #     print(row[0]