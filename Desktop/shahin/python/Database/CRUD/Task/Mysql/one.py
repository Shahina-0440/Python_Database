import mysql.connector
import requests


stream_data=requests.get("https://dummyjson.com/products")
json_data=stream_data.json()

products_list=json_data["products"]
data=[]
for product in products_list:
    data.append((product["id"],product["title"],product["price"],product["brand"],))



db=mysql.connector.connect(host="localhost",user="root",password="Baba@2121",database="api_products")
cur=db.cursor()
sql_st1='''
create table products(pid int,pname varchar(100),price int,brand varchar(32));
'''
cur.execute(sql_st1)
sql_st2='''
insert into products(pid,pname,price,brand) values(%s,%s,%s,%s);
'''
cur.executemany(sql_st2,data)
db.commit()

cur.close()
db.close()