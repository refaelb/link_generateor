from unicodedata import name
import pymongo
token_user=34




myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fixpay"]
mycol = mydb["fixpay_users"]

mydict = { "user_name": "John", "user_id": "315346" , '$set': 0}

# x = mycol.update(mydict)
mycol.update_many({'user_name':'John'}, {"$set": {"count_orders":0}}, upsert=False)


# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["fixpay"]

# mydoc = mycol.inn
# # print (mydoc["name"])
# for x in mydoc:
# #   print(x["name"])
#   if x["name"] == token_user:
#     count_orders=x["count_orders"]
#     print (count_orders)
#     break


