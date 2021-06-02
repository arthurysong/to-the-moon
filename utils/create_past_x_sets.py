def create_past_x_sets(klines):
  """accept x amount of klines and return sets of 40 past points
  
  klines is an array of klines
  return is an array of string (which rep 40 sets)"""

  num_of_klines_for_set = 40
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


