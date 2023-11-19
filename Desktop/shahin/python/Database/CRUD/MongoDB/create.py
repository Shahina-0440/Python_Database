import pymongo
client=pymongo.MongoClient()
db=client["CRUDpymongoDatabase"]
coll=db["CRUD"]
