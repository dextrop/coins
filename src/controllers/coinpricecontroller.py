import requests, json, os
from django.core.exceptions import ValidationError
file = "/root/coins/coins.json"

class CoinPriceController():

    def update_price(self):
        resp = requests.get("https://dev-api.shrimpy.io/v1/exchanges/kucoin/ticker")
        prices = {}
        try:
            for element in resp.json():
                curr = {
                    "prices": [round(float(element["priceUsd"]), 5)],
                    "name": element["name"],
                    "symbol": element["symbol"]
                }
                prices[curr["symbol"]] = curr
        except Exception as e:
            f = open(file, "r")
            data = json.load(f)
            return data

        resp = {
            "coins": []
        }

        if not os.path.exists(file):
            for element in prices:
                resp["coins"].append(prices[element])
        else:
            f = open(file, "r")
            data = json.load(f)
            for element in data["coins"]:
                element["prices"].append(prices[element["symbol"]]["prices"][0])
                element["prices"] = element["prices"][(len( element["prices"]) - 10 ):len( element["prices"])]
            resp = data

        with open(file, 'w') as json_file:
            json.dump(resp, json_file)

        return resp

    def get_coin_price(self):
        if not os.path.exists(file):
            raise ValidationError("Updates not available")
        else:
            f = open(file, "r")
            data = json.load(f)
            return data

    def update_coin_price(self):
        return self.update_price()