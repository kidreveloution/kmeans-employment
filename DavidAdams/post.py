import alpaca_trade_api as tradeapi
import requests, json
from config import *

api = tradeapi.REST(
    key_id= API_KEY,
    secret_key=API_SECRET_Key,
    base_url='https://paper-api.alpaca.markets'
)
account = api.get_account()
print(account.status)

order=api.submit_order(
                symbol='AAPL',
                qty='1',
                side='buy',
                type = 'market',
                time_in_force='gtc',
            )