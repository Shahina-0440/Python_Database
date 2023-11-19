import requests
import mysql.connector
import csv

stream_data=requests.get("https://dummyjson.com/products")
json_data=stream_data.json()

products_list=json_data["products"]
data=[]
for product in products_list:
    data.append([product["id"],product["title"],product["price"],product["brand"]])


fp=open("products.csv","w",newline="")
csv_writer=csv.writer(fp)
csv_writer.writerows(data)
