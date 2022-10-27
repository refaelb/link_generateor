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
    print (data)
    a = validate(data)
    return a



def validate(data):
    json_data=json.loads(data)
    print (json_data)
    token_user = int(json_data["token_user"])
    amount = int(json_data["amount"])
    count_links = int(json_data["count_links"])
    
    return read_from_mongo(token_user, amount, count_links)

def read_from_mongo(token_user, amount, count_links):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["links"]
    myquery = { "name": token_user }
    # mydoc = mycol.find().sort(token_user, -1).limit(1)
    # # print (mydoc)
    # count_orders=mydoc["count_orders"]
    mydoc = mycol.find({"name":token_user}).sort("count_orders", -1).limit(1)
    # print ('123 ' + mydoc["name"])
    
    if mydoc[0]:
        count_orders=mydoc[0]["count_orders"]
    else :
        count_orders=0
    print (count_orders)
    count_orders=count_orders+1
    out = []
    for i in range (count_links):
        out.append(api_createor(token_user, amount, count_links))
    print (out)
    write_to_mongo(token_user, amount, count_links, out, count_orders)
    return (out)



def api_createor(token_user, amount, count_links):
    url = "https://stoplight.io/mocks/coinpay/api-2-0/59787578/api/integration/link/createLink/v1"

    payload = json.dumps({
    "CurrencyCode": "BTC",
    "IdCurrencyPay": 6,
    "Amount": amount,
    "IdReference": token_user,
    "Address": "1AkfP72SZiM1zxwkk5GttXrLi7mmTAmFmk"
    })
    headers = {
    'Authorization': 'Bearer  42c1823c7c014de7e19d6d8ca76a1aa43e08d1a5bd420baa1ca271f3bb486e64',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Cookie': 'GCLB=CPqyg5CBhdrDyQE; __cf_bm=P0iGBOYWMhbvIZfWmdIhESTSvzmrlHkCmW70NdDZFTM-1666557847-0-AZ9hUutXbZFk/t5lZ7qJEefSVbiTlpQTXEp8lS7lnNeNUbbFLh42SXVA0VebZzIyWuv0Us/vtyvwsduliBq/2Dc='
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.content)
    json_data=json.loads(response.content)
    links=json_data['Data']
    return links

def write_to_mongo(token_user, amount, count_links,links, count_orders):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    print("Date and time is:", dt)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["links"]
    mydict = { "name": token_user, "links": links , "count_orders": count_orders, "amount": amount, "time": dt }

    x = mycol.insert_one(mydict)
    return(links)
