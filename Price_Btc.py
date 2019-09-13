import time
import json
import requests
"""
Some api pages
https://bitpay.com/bitcoin-payment-gateway-api
https://blockchain.info/api
https://localbitcoins.com/api-docs/public/
https://www.bitstamp.net/api/
https://coinbase.com/docs/api/overview
https://coinbase.com/api/doc/1.0/prices/buy.html
https://coinbase.com/api/v1/prices/spot_rate
https://www.kraken.com/help/api
https://www.bitfinex.com/pages/api
https://www.cryptsy.com/pages/api
http://bitcoincharts.com/about/markets-api/
https://www.bitfinex.com/pages/api
"""

'''
def btstamp():
    bitStampTick = requests.get(
        'https://www.bitstamp.net/api/ticker/')
    return bitStampTick.json()['last']  # replace last with timestamp etc


def btceBU():
    btceBtcTick = requests.get(
        'https://btc-e.com/api/2/btc_usd/ticker')
    # replace last with updated etc
    return btceBtcTick.json()['ticker']['last']


def btceBL():
    btceLtcTick = requests.get(
        'https://btc-e.com/api/2/ltc_btc/ticker')
    # replace last with updated etc
    return btceLtcTick.json()['ticker']['last']
'''


def bitfinex():
    bitFinexTick = requests.get(
        "https://api.bitfinex.com/v1/ticker/btcusd")
    return bitFinexTick.json()['last_price']


def coinbase():
    # replace buy with spot_rate, sell etc
    coinBaseTick = requests.get(
        'https://api.coinbase.com/v2/prices/BTC-USD/buy')
    # replace amount with currency etc
    return (coinBaseTick.json()['data'])['amount']


'''
def kraken():
    krakenTick = requests.post('https://api.kraken.com/0/public/Ticker', data=json.dumps({"pair": "XXBTZUSD"}),
                               headers={"content-type": "application/json"})
    return krakenTick.json()['result']['XXBTZUSD']['c'][0]
'''

while True:
    # btstampUSDLive = float(btstamp())
    # btceUSDLive = float(btceBU())
    # btceLTCinBTCLive = float(btceBL())
    coinbUSDLive = float(coinbase())
    # krakenUSDLive = float(kraken())
    bitfinexUSDLive = float(bitfinex())

    # print("Bitstamp Price in USD =", btstampUSDLive)
    # print("BTC-e Price in USD =", btceUSDLive)
    print("Coinbase Price in USD =", coinbUSDLive)
    # print("Kraken Price in USD =", krakenUSDLive)
    print("Bitfinex Price in USD =", bitfinexUSDLive)
    print("=-" * 30)
    print("BTC USD Average = ", (coinbUSDLive + bitfinexUSDLive) / 5)
    # print("difference betweeen coinbase and bitstamp", (coinbUSDLive - btstampUSDLive))
    # print("BTC-e LTC Price in BTC", btceLTCinBTCLive)
    # print("BTC-e LTC Price in USD =", btceLTCinBTCLive * btceUSDLive, "USD")
    print()
    print()
    print("=-"*10)
    print()
    # 120 equals two minutes, you can ping it every second by putting a 1 in here
    time.sleep(120)
