from urllib.request import urlopen
import ssl
import json
import os
import random
import urllib
# This restores the same behavior as before.
context = ssl._create_unverified_context()

os.system('clear')
a = input("Contenido a buscar: ")
searchURL = "https://es.wikipedia.org/w/api.php?action=opensearch&format=json&search=" + a

with urlopen(searchURL, context=context) as response:
    source = response.read()
data = json.loads(source)


def goWiki():
    pass


def urldecode(str):
    return urllib.parse.unquote(str)


c = random.randint(1, len(data[1])-1)
print(data[1][c])
print(data[2][c])
print(urldecode(data[3][c]))


# print(json.dumps(data, indent=2))


'''
usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))
'''
