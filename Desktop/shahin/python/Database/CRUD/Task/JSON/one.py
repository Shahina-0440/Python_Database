import requests
import json
import mysql.connector


stream_data=requests.get("https://dummyjson.com/products")
json_data=stream_data.json()

products_list=json_data["products"]
data=[]
for product in products_list:
    data.append({"id":product["id"],"name":product["title"],"price":product["price"],"brand":product["brand"]})


fp=open("products.json","w")
json.dump(data,fp,indent=2)