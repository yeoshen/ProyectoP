import json
import requests

candle = 5
broker = 'BINANCE'
market = 'BTCUSDT'

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://scanner.tradingview.com/crypto/scan"

a = {
    "symbols": {
        "tickers": ["{}:{}".format(broker, market)],
        "query": {"types": []}
    },
    "columns": [
        "Recommend.Other|{}".format(candle),
        "Recommend.All|{}".format(candle),
        "Recommend.MA|{}".format(candle),
        "RSI|{}".format(candle),
        "RSI[1]|{}".format(candle),
        "Stoch.K|{}".format(candle),
        "Stoch.D|{}".format(candle),
        "Stoch.K[1]|{}".format(candle),
        "Stoch.D[1]|{}".format(candle),
        "CCI20|{}".format(candle),
        "CCI20[1]|{}".format(candle),
        "ADX|{}".format(candle),
        "ADX+DI|{}".format(candle),
        "ADX-DI|{}".format(candle),
        "ADX+DI[1]|{}".format(candle),
        "ADX-DI[1]|{}".format(candle),
        "AO|{}".format(candle),
        "AO[1]|{}".format(candle),
        "Mom|{}".format(candle),
        "Mom[1]|{}".format(candle),
        "MACD.macd|{}".format(candle),
        "MACD.signal|{}".format(candle),
        "Rec.Stoch.RSI|{}".format(candle),
        "Stoch.RSI.K|{}".format(candle),
        "Rec.WR|{}".format(candle),
        "W.R|{}".format(candle),
        "Rec.BBPower|{}".format(candle),
        "BBPower|{}".format(candle),
        "Rec.UO|{}".format(candle),
        "UO|{}".format(candle),
        "EMA5|{}".format(candle),
        "close|{}".format(candle),
        "SMA5|{}".format(candle),
        "EMA10|{}".format(candle),
        "SMA10|{}".format(candle),
        "EMA20|{}".format(candle),
        "SMA20|{}".format(candle),
        "EMA30|{}".format(candle),
        "SMA30|{}".format(candle),
        "EMA50|{}".format(candle),
        "SMA50|{}".format(candle),
        "EMA100|{}".format(candle),
        "SMA100|{}".format(candle),
        "EMA200|{}".format(candle),
        "SMA200|{}".format(candle),
        "Rec.Ichimoku|{}".format(candle),
        "Ichimoku.BLine|{}".format(candle),
        "Rec.VWMA|{}".format(candle),
        "VWMA|{}".format(candle),
        "Rec.HullMA9|{}".format(candle),
        "HullMA9|{}".format(candle),
        "Pivot.M.Classic.S3|{}".format(candle),
        "Pivot.M.Classic.S2|{}".format(candle),
        "Pivot.M.Classic.S1|{}".format(candle),
        "Pivot.M.Classic.Middle|{}".format(candle),
        "Pivot.M.Classic.R1|{}".format(candle),
        "Pivot.M.Classic.R2|{}".format(candle),
        "Pivot.M.Classic.R3|{}".format(candle),
        "Pivot.M.Fibonacci.S3|{}".format(candle),
        "Pivot.M.Fibonacci.S2|{}".format(candle),
        "Pivot.M.Fibonacci.S1|{}".format(candle),
        "Pivot.M.Fibonacci.Middle|{}".format(candle),
        "Pivot.M.Fibonacci.R1|{}".format(candle),
        "Pivot.M.Fibonacci.R2|{}".format(candle),
        "Pivot.M.Fibonacci.R3|{}".format(candle),
        "Pivot.M.Camarilla.S3|{}".format(candle),
        "Pivot.M.Camarilla.S2|{}".format(candle),
        "Pivot.M.Camarilla.S1|{}".format(candle),
        "Pivot.M.Camarilla.Middle|{}".format(candle),
        "Pivot.M.Camarilla.R1|{}".format(candle),
        "Pivot.M.Camarilla.R2|{}".format(candle),
        "Pivot.M.Camarilla.R3|{}".format(candle),
        "Pivot.M.Woodie.S3|{}".format(candle),
        "Pivot.M.Woodie.S2|{}".format(candle),
        "Pivot.M.Woodie.S1|{}".format(candle),
        "Pivot.M.Woodie.Middle|{}".format(candle),
        "Pivot.M.Woodie.R1|{}".format(candle),
        "Pivot.M.Woodie.R2|{}".format(candle),
        "Pivot.M.Woodie.R3|{}".format(candle),
        "Pivot.M.Demark.S1|{}".format(candle),
        "Pivot.M.Demark.Middle|{}".format(candle),
        "Pivot.M.Demark.R1|{}".format(candle)
    ]
}

resp = requests.post(url, headers=headers, data=json.dumps(a)).json()

signal = resp["data"][0]["d"][1]

# b = json.dumps(a, indent=4)  # , sort_keys=True)

print(signal)
