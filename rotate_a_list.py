# given a list, rotate the list by a number of spaces, k
# input: list = ['a', 'b', 'c', 'd'], k = 3
# output: ['d', 'a', 'b', 'c']
#
#
# edge cases: if k <= 0           ==> k can only be +ve integers and if k == 0, return list as is
#             if k > len(list)    ==> return list
#
#
# space = O(n)
# time = O(n)
def rotate_list(list, k):
  if k <= 0:
    return list
  if len(list) < k:
    return list
  return list[-k:] + list[:-k]

print(rotate_list(['a', 'b', 'c', 'd', 'e'], 3))
print(rotate_list(['a', 'b', 'c', 'd', 'e', 'f'], 2))
print(rotate_list(['a', 'b', 'c', 'd'], 1))
#
#
#
#
#
# optimized solution
# space = O(1)
def rotate_list_2(list, k):
  if k <= 0:
    return list
  if len(list) < k:
    return list
  reverse(list, 0, k-1)
  reverse(list, k, len(list)-1)
  reverse(list, 0, len(list)-1)
  return list

def reverse(list, low, high):
  while low < high:
    list[low], list[high] = list[high], list[low]
    high -= 1
    low += 1
  return list

print(rotate_list_2(['a', 'b', 'c', 'd', 'e'], 3))
print(rotate_list_2(['a', 'b', 'c', 'd', 'e', 'f'], 2))
print(rotate_list_2(['a', 'b', 'c', 'd'], 1))
#
#
#
#
#
# variant: given a sorted list rotated k times, return the index where the unrotated list begin
# input: list = ['c', 'd', 'e', 'f', 'a']
# output: 4 - index of smallest element in list

# time = O(n)
# space = O(1)
def rotation_point(list):
  rotation_idx = 0
  for i in range(len(list)):
    if list[i] < list[rotation_idx]:
      rotation_idx  = i
  return rotation_idx

print(rotation_point(['c', 'd', 'e', 'f', 'a', 'b']))
print(rotation_point([13, 8, 9, 10, 11]))


# binary search approach
# time = O(logn)
def rotation_point_2(list):
  low = 0
  high = len(list) -1

  while low <= high:
    mid = (low+high) // 2
    mid_next = (mid+1) % len(list)
    mid_previous = (mid-1) % len(list)

    if(list[mid] < list[mid_previous]) and (list[mid] < list[mid_next]):
      return mid
    if list[mid] < list[high]:
      high = mid-1
    else:
      low = mid+1

print(rotation_point_2(['c', 'd', 'e', 'f', 'a', 'b']))
print(rotation_point_2([13, 8, 9, 10, 11]))