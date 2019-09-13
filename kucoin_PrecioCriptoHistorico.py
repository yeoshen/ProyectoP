from datetime import datetime
import dateparser
import pytz
from kucoin.client import Client
import json


def date_to_seconds(date_str):
    """Convert UTC date to seconds

    If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

    See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/

    :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
    :type date_str: str
    """
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)

    # parse our date string
    d = dateparser.parse(date_str)
    # if the date is not timezone aware apply UTC timezone
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # return the difference in time
    return int((d - epoch).total_seconds())


def get_historical_klines_tv(symbol, interval, start_str, end_str=None):
    """Get Historical Klines from Kucoin (Trading View)

    See dateparse docs for valid start and end string formats http://dateparser.readthedocs.io/en/latest/

    If using offset strings for dates add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"

    :param symbol: Name of symbol pair e.g BNBBTC
    :type symbol: str
    :param interval: Trading View Kline interval
    :type interval: str
    :param start_str: Start date string in UTC format
    :type start_str: str
    :param end_str: optional - end date string in UTC format
    :type end_str: str

    :return: list of OHLCV values

    """

    # init our array for klines
    klines = []
    client = Client("", "", "")

    # convert our date strings to seconds
    start_ts = date_to_seconds(start_str)

    # if an end time was not passed we need to use now
    if end_str is None:
        end_str = 'now UTC'
    end_ts = date_to_seconds(end_str)

    kline_res = client.get_kline_data(symbol, interval, start_ts, end_ts)

    # print(kline_res)

    # check if we got a result
    if 't' in kline_res and len(kline_res['t']):
        # now convert this array to OHLCV format and add to the array
        for i in range(1, len(kline_res['t'])):
            klines.append((
                kline_res['t'][i],
                kline_res['o'][i],
                kline_res['h'][i],
                kline_res['l'][i],
                kline_res['c'][i],
                kline_res['v'][i]
            ))

    # finally return our converted klines
    return klines


def save_historical_klines_file(symbol, interval, start, end):

    klines = get_historical_klines_tv(symbol, interval, start, end)

    # open a file with filename including symbol, interval and start and end converted to seconds
    with open(
        "Kucoin_{}_{}_{}-{}.json".format(
            symbol,
            interval,
            date_to_seconds(start),
            date_to_seconds(end)
        ),
        'w'  # set file write mode
    ) as f:
        f.write(json.dumps(klines))


'''
print(date_to_seconds("January 01, 2018"))
print(date_to_seconds("11 hours ago UTC"))
print(date_to_seconds("now UTC"))


# fetch 1 minute klines for the last day up until now
klines = get_historical_klines_tv("KCS-BTC", "1", "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = get_historical_klines_tv(
    "NEO-BTC", "30", "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = get_historical_klines_tv("XRP-BTC", "W", "1 Jan, 2017")
'''


symbol = "KCS-BTC"
start = "1 Dec, 2017"
end = "1 Jan, 2018"
interval = "30"
save_historical_klines_file(symbol, interval, start, end)
