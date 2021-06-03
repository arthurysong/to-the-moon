#! /usr/bin/python3

import requests
from pathlib import Path

BYBIT_API = "https://api.bybit.com"
TIME_FRAME = 15 # 15 min interval
FROM_TIMESTAMP = 1542211200 # this is the earliest timestamp avail in BYBITAPI
SYMBOL = "BTCUSD"

base_path = Path(__file__).parent
file_path = (base_path / "../data/raw_klines_data.m").resolve()
raw_klines_data = open(file_path, "w")

klines = []
x = 0

while x < 600:
  r = requests.get(f"{BYBIT_API}/v2/public/kline/list?symbol={SYMBOL}&interval={TIME_FRAME}&from={FROM_TIMESTAMP}")
  json = r.json()
  x += len(json["result"])

  for kline in json["result"]:
    str = f'{kline["open_time"]} {kline["open"]} {kline["high"]} {kline["low"]} {kline["close"]} {kline["volume"]} {kline["turnover"]}'

    klines.append(str)

raw_klines_data.write("\n".join(klines))
