from unicodedata import name
import pymongo
token_user=34
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["links"]

mydoc = mycol.find().sort("count_orders", -1)
# print (mydoc["name"])
for x in mydoc:
#   print(x["name"])
  if x["name"] == token_user:
    count_orders=x["count_orders"]
    print (count_orders)
    break


