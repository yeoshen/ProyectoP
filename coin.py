from urllib.request import urlopen
import ssl
import json
import os
import random
import urllib
import requests


def url_API(searchURL):
    context = ssl._create_unverified_context()
    with urlopen(searchURL, context=context) as response:
        source = response.read()
    return json.loads(source)


def precio_BTC(date_str):
    # date_str = YYYY-MM-DD
    btc_prices = f'https://api.coindesk.com/v1/bpi/historical/close.json?start={date_str}&end={date_str}'
    a = url_API(btc_prices)
    print(a['bpi'])
    return float(a['bpi'][date_str])


def precios_BTC(date1, date2):
    # format date1, date2 = YYYY-MM-DD
    # Return a dictionary with BTC prices
    return requests.get(
        f'https://api.coindesk.com/v1/bpi/historical/close.json?start={date1}&end={date2}'
    ).json()['bpi']


# This restores the same behavior as before.
os.system('clear')

# Price BTC by range date
btc_price = 'https://api.coinmarketcap.com/v1/ticker/'
r = dict()
r = url_API(btc_price)[0]
print(r['symbol'] + " " + r['price_usd'])
# print(type(r))

#x = precio_BTC('2018-11-18')
# print(x)

date1 = '2018-01-01'
date2 = '2019-12-31'
a = precios_BTC(date1, date2)


for key, value in a.items():
    print(key, " ", value)
