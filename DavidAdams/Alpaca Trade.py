import requests, json
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID": API_KEY, 'APCA-API-SECRET-KEY': API_SECRET_Key}
def get_acoount():
    r = requests.get(ACCOUNT_URL , headers = HEADERS)
    return json.loads(r.content)

print(get_acoount())
def create_order(symbol,qty,side,type,time_in_force):
        data = {
            "symbol" : symbol,
            "qty" : qty,
            "side" : side,
            "type" : type,
            "time_in_foce": time_in_force
        }
        r = requests.post(ORDERS_URL, json = data, headers = HEADERS)

        return json.loads(r.content)


response = create_order("AAPL",100, "buy","market",'gtc')

print(response)