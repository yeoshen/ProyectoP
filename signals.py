import requests
import json
import time
import datetime


def mlog(market, *text):
    text = [str(i) for i in text]
    text = " ".join(text)

    datestamp = str(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3])

    print("[{} {}] - {}".format(datestamp, market, text))


def get_signal(market, candle, broker):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://scanner.tradingview.com/crypto/scan"

    payload = {
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
            "EMA10|{}".format(candle),
            "close|{}".format(candle),
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

    resp = requests.post(url, headers=headers, data=json.dumps(payload)).json()

    signal = resp["data"][0]["d"][1]

    return signal


if __name__ == "__main__":

    broker = 'BINANCE'
    market = "ETHUSDT"
    candle = 1  # Represented in minutes
    ms = ''

    mlog(market, "Getting TV signal for {}, {} minute candle.".format(market, candle))

    signal = get_signal(market, candle, broker)
    if signal is None:
        signal = 0

    if signal > 0 and signal < 0.4:
        ms = 'Comprar'
    elif signal > 0.4:
        ms = 'Compra Fuerte'
    elif signal == 0:
        ms = 'Neutral'
    elif signal < 0 and signal > -0.4:
        ms = 'Vender'
    elif signal < -0.4:
        ms = 'Venta Fuerte'

    mlog(market, signal, " ", ms)
