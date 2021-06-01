import requests
import pprint

print("hi");

BYBIT_API = "https://api.bybit.com"

r = requests.get(f"{BYBIT_API}/v2/public/orderBook/L2?symbol=BTCUSD")

pprint(r.json())