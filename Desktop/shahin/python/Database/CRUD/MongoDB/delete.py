import pymongo
client=pymongo.MongoClient()
db=client["CRUDpymongoDatabase"]
coll=db["CRUD"]

coll.delete_one({"name": "John Doe"})