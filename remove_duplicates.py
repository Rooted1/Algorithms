# given a sorted list of values, return a list holding the same values in the same order with all duplicates removed
# input: list = ['a', 'a', 'x', 'x', 'x', 'g', 't', 't']
# output: ['a', 'x', 'g', 't']

# time = O(n)
# space = O(n)
def remove_dups(list):
  new_list = []
  for i in range(len(list)):
    if list[i] not in new_list:
      new_list.append(list[i])
  return new_list

print(remove_dups(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']))
#
#
#
#
#
# optimized - move all duplicates to end of list
# space - O(1)
def remove_dups_2(list):
  unique = 0
  for i in range(len(list) - 1):
    if list[i] != list[i+1]:
      list[i], list[unique] = list[unique], list[i]
      unique += 1
  list[len(list)-1], list[unique] = list[unique], list[len(list)-1]
  return list[:(unique+1)]

print(remove_dups_2(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']))