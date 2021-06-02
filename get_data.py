import requests
from pprintpp import pprint
from datetime import datetime
from utils.create_past_x_sets import create_past_x_sets
from utils.convert_sets_to_labeled_data import convert_sets_to_labeled_data

BYBIT_API = "https://api.bybit.com"

data = open("data.m", "w")
klines = []

x = 0

# gets 600 klines from API from some arbitrary time stamp
# maps 600 points into sets of X klines, where x is 40

# example of 20 points mapped to sets of 3
# so [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# => [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], ...]

while x < 600:
  r = requests.get(f"{BYBIT_API}/v2/public/kline/list?symbol=BTCUSD&interval=15&from=1542211200")
  json = r.json()
  x += len(json["result"])

  for kline in json["result"]:
    str = f'{kline["open"]} {kline["high"]} {kline["low"]} {kline["close"]} {kline["volume"]} {kline["turnover"]}'

    klines.append(str)

print(len(klines))

# pprint(create_past_x_sets(klines))
# data_str = "\n".join(create_past_x_sets(klines))
# data.write(data_str)

# pprint(convert_sets_to_labeled_data(create_past_x_sets(klines)))

data_str = "\n".join(convert_sets_to_labeled_data(create_past_x_sets(klines)))
data.write(data_str)
