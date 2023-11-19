import requests
import mysql.connector

stream_data=requests.get("https://dummyjson.com/users")
json_data=stream_data.json()

users_list=json_data["users"]
print(type(json_data))

data=[]
for user in users_list:
    data.append((user["id"],user["firstName"],user["age"],user["email"],user["gender"],))
try:
        db=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="api_user")
        cur=db.cursor()
        sql_st='''
        create table users(uid int,uname varchar(32),uage int,uemail varchar(40),ugender varchar(10))
        '''
        cur.execute(sql_st)
        db.commit()
        print("Table created succesfully...")
except mysql.connector.DatabaseError as err:
    print(err)
finally:
    if db:
        db.close()
    if cur:
        cur.close()



