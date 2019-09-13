import json
import requests

coinBaseTick = requests.get(
    'https://api.coinbase.com/v2/prices/BTC-USD/buy')
# replace amount with currency etc

print(type(coinBaseTick.json()['data']))
