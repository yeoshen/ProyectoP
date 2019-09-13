import requests

globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

# get data from globalURL
request = requests.get(globalURL)
data = request.json()
globalMarketCap = data['total_market_cap_usd']
globalMarketCap = round(globalMarketCap / 1000000, 2)
request = requests.get(tickerURL)
data = request.json()

d = [[registro['symbol'], registro['price_usd']] for registro in data]


def buscar_Precio_Moneda(moneda: str):
    resp = [i[1] for i in d if i[0] == moneda]
    if not resp:
        r = 0
    else:
        r = resp[0]
    return r


print(buscar_Precio_Moneda('BTC'))
