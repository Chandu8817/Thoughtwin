
import csv
import mysql.connector

mydb= mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="demodata"
)
val=[]

file=input("file name")
    # file='demodata.csv'


try:
    with open(file, mode="r") as csv_file:
        csv_read=csv.reader(csv_file)
        line_count=0
        for x in csv_read:
            if line_count==0:
                # print(x)
                line_count += 1
            else:          
                tableval= tuple(x)
                val.append(tableval)
                line_count+=1
                
except:
    print("file not valid")



    # sql = "INSERT INTO user (name, city, email ,mob ) VALUES (%s , %s , %s, %s)"
    # sql="INSERT INTO employ_data (name, Date of Birth, Date of Joining, Email, Mobile Number) VALUES (%s,%s,%s,%s,%s)"
    # vsl =('gfjkld', '2002-03-09', '2020-03-10', 'fghgfvghh@vvggdfgd.com', '4678956')

insertdata=mydb.cursor()


insertdata.execute("SELECT * FROM employ_data ")
res=insertdata.fetchall()

count=0
email_list=[]
mob_list=[]


for o in res:

    email_list.append(o[4])
    mob_list.append(o[5])
    # print(o[4])


for i in val:
    mob=int(i[4])
    if i[3] in email_list:
        print("Email already available")
        print(i[3])
        
    elif mob in mob_list:
        print("mobile number already available")
        print(i[4])
        
        
    else:
        sql="INSERT INTO employ_data ( name, dob, doj, email, mobile) VALUES (%s,%s,%s,%s,%s)"
        insertdata.executemany(sql,val)
        mydb.commit()
        print(insertdata.rowcount,'inserted successfully')
        
        # print("yes")
