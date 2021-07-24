# program to return index of maximum value and max value in an unsorted list using linear search

def maximum_value(list):
  maximum_value_index = None
  for idx in range(len(list)):
    if maximum_value_index is None or list[idx] > list[maximum_value_index]:
      maximum_value_index = idx 
  return maximum_value_index, list[maximum_value_index]

print(maximum_value([88, 93, 75, 100, 80, 67, 71, 92, 90, 83]))