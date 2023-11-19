import requests
import json
import pymongo


stream_data=requests.get("https://dummyjson.com/products")
json_data=stream_data.json()

products_list=json_data["products"]
data=[]
for product in products_list:
    data.append({"id":product["id"],"name":product["title"],"price":product["price"],"brand":product["brand"]})

client=pymongo.MongoClient()
db=client["api_products"]
coll=db["products"]

coll.insert_many(data)