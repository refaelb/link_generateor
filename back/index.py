from flask import Flask, request ,Response
import json
import os
import requests
from flask import render_template





app = Flask(__name__)


@app.route('/' , methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/create_links', methods=['POST'])
def pipline_api():
    data = (request.data)
    print (data)
    return validate(data)


def validate(data):
    json_data=json.loads(data)
    print (json_data)
    count_links = (json_data["count_links"])
    count = (json_data["count"])
    id_user = (json_data["id_user"])
    out = []
    for i in range (count):
        out.append(api_createor(count_links, id_user))
    print (out)
    return out
def api_createor(count_links, id_user):
    url = "https://stoplight.io/mocks/coinpay/api-2-0/59787578/api/integration/link/createLink/v1"

    payload = json.dumps({
    "CurrencyCode": "BTC",
    "IdCurrencyPay": 6,
    "Amount": count_links,
    "IdReference": id_user,
    "Address": "1AkfP72SZiM1zxwkk5GttXrLi7mmTAmFmk"
    })
    headers = {
    'Authorization': 'Bearer Bearer 42c1823c7c014de7e19d6d8ca76a1aa43e08d1a5bd420baa1ca271f3bb486e64',
    'Content-Type': 'application/json',
    'Cookie': 'GCLB=CPqyg5CBhdrDyQE; __cf_bm=P0iGBOYWMhbvIZfWmdIhESTSvzmrlHkCmW70NdDZFTM-1666557847-0-AZ9hUutXbZFk/t5lZ7qJEefSVbiTlpQTXEp8lS7lnNeNUbbFLh42SXVA0VebZzIyWuv0Us/vtyvwsduliBq/2Dc='
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.content)
    json_data=json.loads(response.content)
    links=json_data['Data']
    return links
