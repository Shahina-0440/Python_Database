import pymongo
client=pymongo.MongoClient()
db=client["CRUDpymongoDatabase"]
coll=db["CRUD"]
data_to_insert = {"name": "John Doe", "age": 25, "city": "New York","avail":True}
coll.insert_one(data_to_insert)