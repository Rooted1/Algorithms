# write a function that searches a sorted list of numbers and returns a target value
# input - list and target
# output - index of target if it exists 

def binary_search(list, target):
  return helper(list, 0, len(list), target)
  

def helper(list, left_pointer, right_pointer, target):

  if left_pointer >= right_pointer:
    return None

  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = list[mid_idx]

  if mid_val == target:
    return mid_idx 
  if mid_val > target:
    return helper(list, left_pointer, mid_idx, target)
  if mid_val < target:
    return helper(list, mid_idx+1, right_pointer, target)
  return mid_idx

print(binary_search([77, 80, 102, 123, 288, 300, 540], 102))
print(binary_search([], 102))