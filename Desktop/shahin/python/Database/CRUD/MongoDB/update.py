import pymongo
client=pymongo.MongoClient()
db=client["CRUDpymongoDatabase"]
coll=db["CRUD"]

coll.update_one({"name": "John Doe"},{"$set":{"age":30}})