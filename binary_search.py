# functions searches a sorted list and returns the index of the target value

def binary_search(list, target):
  if not list:
    return None

  return bin_search_helper(list, 0, len(list), target)
  

def bin_search_helper(list, left_pointer, right_pointer, target):
  if left_pointer >= right_pointer:
    return None

  print("Left pointer is: {0} \nRight pointer is:{1}".format(left_pointer, right_pointer))

  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = list[mid_idx]
  print("mid_idx", mid_idx, "\n")

  if mid_val == target:
    print("Element at index {0} is {1} - the target value".format(mid_idx, mid_val))
    return mid_idx

  if mid_val > target:
    return bin_search_helper(list, left_pointer, mid_idx, target)
  if mid_val < target:
    return bin_search_helper(list, mid_idx+1, right_pointer, target)



print(binary_search([77, 80, 102, 123, 288, 300, 540], 102), "\n\n")
print(binary_search([77, 80, 102, 123, 288, 300, 540], 288))
print(binary_search([], 5))