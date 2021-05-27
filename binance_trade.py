from binance.websockets import BinanceSocketManager
from binance.exceptions import BinanceAPIException, BinanceWithdrawException
from binance.client import Client

import binance_trade

api_key = ''
api_secret = ''

client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BTCUSDT')
# print(depth)

'''
# place a test market buy order, to place an actual order use the create_order function
order = client.create_test_order(
    symbol='BNBBTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)

# get all symbol prices
prices = client.get_all_tickers()
'''

'''
# withdraw 100 ETH
# check docs for assumptions around withdrawals
try:
    result = client.withdraw(
        asset='ETH',
        address='<eth_address>',
        amount=100)
except BinanceAPIException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("Success")
'''

pp = client.get_products()
print(pp)

"""
# fetch list of withdrawals
withdraws = client.get_withdraw_history()
#r = [amount for amount in withdraws.items()]
print(type(withdraws))
i = 0
num = len(withdraws['withdrawList'])
while i < num:
    for key, value in withdraws['withdrawList'][i].items():
        print(i, ':', key, '=', value)
    i += 1


# fetch list of ETH withdrawals
#eth_withdraws = client.get_withdraw_history(asset='ETH')

# get a deposit address for BTC
address = client.get_deposit_address(asset='BTC')
print(address)

# start aggregated trade websocket for BNBBTC

'''
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something


bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines(
    "BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines(
    "ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = client.get_historical_klines(
    "NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")
'''


"""
