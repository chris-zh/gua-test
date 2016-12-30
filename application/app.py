from flask import Flask
from flask import render_template
import json
from flask import request
from flask import jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/test")
def test():
    return render_template("seller.html")


@app.route("/sellers", methods=["post", "get"])
def sellers():
    data = {
        "businessId": 7
    }
    r = requests.post('http://qa.backend-product.soa.yeshj.com/QueryProduct/Sellers', json=json.dumps(data))
    print(r.text)
    return jsonify(r.text)


@app.route("/api/admin/user/query", methods=["post", "get"])
def queryUser():
    text = request.get_json()
    userName = text.get('userName', '')
    user = {
        'userId': 1,
        'userName': userName,
        'age': 28,
    }
    userList = [
        user, user, user, user, user
    ]
    return jsonify(userList)


@app.route("/Sellers", methods=["post", "get"])
def seller2():
    text = request.get_json()  # text = {"BusinessId":2}
    bid = text.get('BusinessId', '')
    print('businessId: ', bid)
    sellers = {}
    if bid == '2':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    elif bid == '7':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    elif bid == 'null':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"},
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    else:
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"},
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    return json.dumps(sellers)


@app.route("/seller233", methods=["post", "get"])
def seller233():
    text = request.get_json()  # text = {"BusinessId":2}
    try:
        bid = text.get('BusinessId', '')
    except:
        bid = 'null'
    print('businessId: ', bid)
    sellers = {}
    if bid == '2':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    elif bid == '7':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    elif bid == 'null':
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"},
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    else:
        sellers = {
            "data": {
                "total": 4,
                "Sellers": [
                    {"SellerId": 1001, "SellerName": "网校机构1", "SettlementName": "蒋干"},
                    {"SellerId": 1002, "SellerName": "网校机构2", "SettlementName": "蒋干"},
                    {"SellerId": 1, "SellerName": "CC1机构", "SettlementName": "蒋干"},
                    {"SellerId": 2, "SellerName": "CC2机构", "SettlementName": "蒋干"}
                ]
            },
            "status": 0,
            "message": 'null'
        }
    return jsonify(sellers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
