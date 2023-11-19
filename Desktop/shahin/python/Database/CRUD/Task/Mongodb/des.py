
import pymongo


client=pymongo.MongoClient()
db=client["api_products"]
coll=db["products"]

result = coll.find().sort("id", pymongo.DESCENDING)
for i in result:
    print(i)