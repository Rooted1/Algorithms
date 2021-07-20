# given a list of integers, return maximum sum possible from a contiguous sub-list. A contiguous sub-list is an #uninterrupted portion of the list (up to and including the entire list)
#
# input: list = [1,-7, 2, 15, -11, 2]
# output: 17 
# because sum of sub-list list[2:4] =17

# time = O(n^3) - two loops O(n^2) and each copy in the inner loop O(n)
# space = O(n)
def max_sub_sum(list):
  max_sum = list[0]

  for i in range(len(list)):
    for j in range(i+1, len(list)):
      sub_sum = list[i:j +1]
      print(sub_sum)
      if sum(sub_sum) > max_sum:
        max_sum = sum(sub_sum)
  return max_sum 

print(max_sub_sum([1, -7, 2, 15, -11, 2]))
#
#
#
#
#
# time = O(n)
# space O(1)
def max_sub_sum_2(list):
  if max(list) < 0:
    return max(list)
  max_sum = 0
  max_sum_tracker = 0

  for i in range(len(list)):
    max_sum_tracker += list[i]
    if max_sum_tracker < 0:
      max_sum_tracker = 0
    if max_sum_tracker > max_sum:
      max_sum = max_sum_tracker
  return max_sum

print(max_sub_sum_2([1, -7, 2, 15, -11, 2]))
print(max_sub_sum_2([-1, -1, -2, -4, -5, -9, -12, -13]))
print(max_sub_sum_2([1, 2, 3, 4, 5]))
