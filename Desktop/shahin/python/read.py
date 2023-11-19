import pymongo
client=pymongo.MongoClient()
db=client['db1']
col=db['coll1']
l1=col.find({"name":"shahina"})
for i in l1:
    print(i['name'])