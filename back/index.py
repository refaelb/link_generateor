from flask import Flask, request ,Response
import json
import os
import requests
from flask import render_template
from flask_cors import CORS
import pymongo
from datetime import datetime





app = Flask(__name__)
CORS(app)

@app.route('/' , methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/create_links', methods=['POST'])
def pipline_api():
    data = (request.data)
    # a = validate(data)
    return validate(data)


def validate(data):
    json_data=json.loads(data)
    print (json_data)
    user_name = str(json_data["user_name"])
    amount = int(json_data["amount"])
    count_links = int(json_data["count_links"])
    return(checker(user_name, amount, count_links))

def checker(user_name, amount, count_links):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["fixpay"]
    mycol = mydb["fixpay_users"]
    mydoc = mycol.find({},{"user_name":1, "_id":0})
    names=[]
    for i in mydoc:
        names.append(i["user_name"])
    user_name = str(user_name)
    print(names)
    if user_name in names:
        return read_from_mongo(user_name, amount, count_links)
    else:
        user_name=str(user_name)
        out=[{'Link': f'{user_name} not found plise check your user name and try again'}]
        print (out)
        return out


def read_from_mongo(user_name, amount, count_links):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["fixpay"]
    mycol = mydb["fixpay_users"]
    myquery = { "user_name": user_name }
    mydoc=mycol.find(myquery)
    for x in mydoc:
        print (x['user_name'])
        print (x['count_orders'])
        count_orders=x['count_orders']
        user_id=x['user_id']
        count_orders=count_orders+1
        user_order=int(user_id)+(count_orders)

    out = []
    for i in range (count_links):
        out.append(api_createor(user_id, user_order, amount, count_links))
    print (out)
    write_to_mongo(user_name, user_id, amount, count_links, out, count_orders)
    return (out)


def api_createor(user_id,user_order, amount, count_links):
    url = "https://stoplight.io/mocks/coinpay/api-2-0/59787578/api/integration/link/createLink/v1"

    payload = json.dumps({
    "CurrencyCode": "BTC",
    "IdCurrencyPay": 6,
    "Amount": amount,
    "IdReference": user_order,
    "Address": "1AkfP72SZiM1zxwkk5GttXrLi7mmTAmFmk"
    })
    headers = {
    'Authorization': 'Bearer  42c1823c7c014de7e19d6d8ca76a1aa43e08d1a5bd420baa1ca271f3bb486e64',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Cookie': 'GCLB=CPqyg5CBhdrDyQE; __cf_bm=P0iGBOYWMhbvIZfWmdIhESTSvzmrlHkCmW70NdDZFTM-1666557847-0-AZ9hUutXbZFk/t5lZ7qJEefSVbiTlpQTXEp8lS7lnNeNUbbFLh42SXVA0VebZzIyWuv0Us/vtyvwsduliBq/2Dc='
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_data=json.loads(response.content)
    links=json_data['Data']
    return links

def write_to_mongo(user_name, user_id, amount, count_links,links, count_orders):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    print("Date and time is:", dt)

    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myclient["fixpay"]
    mycol = mydb["links"]
    mydict = { "user_name": user_name, "user_id": user_id, "links": links , "count_orders": count_orders, "amount": amount, "time": dt }
    x = mycol.insert_one(mydict)

    mycol = mydb["fixpay_users"]
    mycol.update_one({'user_name':user_name}, {"$set": {"count_orders":count_orders}}, upsert=False)
    return(links)
# 
# if __name__ == '__main__':
# app.run()