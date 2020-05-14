import pymysql
mydb=pymysql.connect(host="localhost",user="Deepak",passwd="1234",database="python")


# prepare a cursor object using cursor() method
cursor = mydb.cursor()


cursor.execute("select * from stud")
res=cursor.fetchone()
for i in res:
    print(i)

# disconnect from server
mydb.close()