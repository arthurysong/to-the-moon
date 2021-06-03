
def raw_to_nn_data(str):
  klines_arr = str.split('\n')
  
  def without_open_time(str):
    kline_arr = str.split(' ')
    kline_arr = kline_arr[1:]
    return ' '.join(kline_arr)

  klines_arr_without_open_times = list(map(without_open_time, klines_arr))

  nn_str = "\n".join(grouped_sets_to_labeled_data(sets_to_grouped_sets(klines_arr_without_open_times)))

  return nn_str

def grouped_sets_to_labeled_data(unlabled_kline_sets):
  """take n sets of X klines (array) and return labeled sets (array)"""

  labeled_sets = []
  for set in unlabled_kline_sets:

    MIN_PRICE_MOVEMENT = 0.01
    NUM_OF_LAST_KLINES = 10
    last_length = NUM_OF_LAST_KLINES * 6
    last_klines = set.split(" ")[-last_length:] 

    # get open from first and close from last 
    # get total price movement
    # and it should be > 1%
    first_open = float(last_klines[0])
    last_close = float(last_klines[-3])
    price_movement = (last_close - first_open) / first_open

    buy_sell_or_hold = None
    if price_movement > MIN_PRICE_MOVEMENT:
      buy_sell_or_hold = "1" # buy
    elif price_movement < -MIN_PRICE_MOVEMENT:
      buy_sell_or_hold = "0" # sell
    else:
      buy_sell_or_hold = "2" # hold

    all_but_last_klines = set.split(" ")[0:-last_length]
    all_but_last_klines.extend([str(first_open), buy_sell_or_hold])

    labeled_sets.append(" ".join(all_but_last_klines))
  
  return labeled_sets

def sets_to_grouped_sets(klines):
  """accept x amount of klines and return sets of X points
  
  klines is an array of kline strings
  return is an array of string (which rep X sets)"""

  num_of_klines_for_set = 50
  # 51 gets split to 40 1 10
  list1 = klines
  sum_list = []
  i = 1

  while i < num_of_klines_for_set:
    list2 = klines[i:]

    for (item1, item2) in zip(list1, list2):
      sum_list.append(item1 + " " + item2)

    # update for next iteration
    list1 = sum_list
    if i != num_of_klines_for_set - 1:
      sum_list = []
    i += 1

  return sum_list
