def convert_sets_to_labeled_data(unlabled_kline_sets):
  """take n sets of X klines (array) and label using the last kline as either 0 or 1"""

  labeled_sets = []
  for set in unlabled_kline_sets:

    MIN_PRICE_MOVEMENT = 0.01
    # 0 1 2
    # sell buy hold
    # if movement is not more than 1% than hold
    
    # last 6 entries = the last kline
    # should be converted to open and y
    # " ".split(set)[:-6]
    last_kline = set.split(" ")[-6:] # last 6 items
    close = float(last_kline[3])
    open = float(last_kline[0])
    price_movement = (close - open) / open

    buy_sell_or_hold = None
    if price_movement > MIN_PRICE_MOVEMENT:
      buy_sell_or_hold = "1"
    elif price_movement < -MIN_PRICE_MOVEMENT:
      buy_sell_or_hold = "0"
    else:
      buy_sell_or_hold = "2"

    all_but_last = set.split(" ")[0:-6]
    all_but_last.extend([str(open), buy_sell_or_hold])
    # print(all_but_last)

    labeled_sets.append(" ".join(all_but_last))
  
  return labeled_sets

