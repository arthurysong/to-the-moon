import requests
from pprintpp import pprint
from datetime import datetime

print("hi");

BYBIT_API = "https://api.bybit.com"

# r = requests.get(f"{BYBIT_API}/v2/public/orderBook/L2?symbol=BTCUSD")
# r = requests.get(f"{BYBIT_API}/v2/public/tickers")
r = requests.get(f"{BYBIT_API}/v2/public/kline/list?symbol=BTCUSD&interval=15&from=1401602115")
# r = requests.get(f"{BYBIT_API}/v2/public/kline/list?symbol=BTCUSD&interval=1&from=1609486020")
# r = requests.get(f"{BYBIT_API}/v2/public/kline/list?symbol=BTCUSD&interval=1&from=1609486000")
json = r.json()
print(len(json["result"]))
print(json["result"][0])
print(json["result"][-1])

l = json["result"][-1]
f = json["result"][0]
print(l['open_time'] - f['open_time'])

# alright, plan is to store all 15 min candlesticks from 1542211200 



# pprint(r.json())