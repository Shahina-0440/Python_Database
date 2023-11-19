import pymongo
client=pymongo.MongoClient()
db=client['db1']
col=db['coll1']
col.insert_one({"name":"shahina"})
print("inserted succesfully......")