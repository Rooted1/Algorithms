# given a list of integers and a target integer, return a pair of indices whose values sum to the target
#
# input: list = [4, 2, 8, 9, 6] target = 8
# output: [1, 4] ==> list[1] + list[4] = 8
#
#
# edge cases: * if the input contains numbers <= 0
#             * does the order of indices matter in the return list ==> [1, 4] or [4, 1]
#             * should all possible pairs be returned or just the first pair

# time = O(n^2)
# space = O(1)
def pair_sum(list, target):
  for i in range(len(list)):
    for j in range(i, len(list)):
      if list[i] + list[j] == target:
        return [i,j]
  return None

print(pair_sum([1, 2, 3, 4, 5], 6))
print(pair_sum([-1, -1, -2, -4, -5, -9, -12, -13], -21))
print(pair_sum([1, -7, 2, 15, -11, 2], 42))
print(pair_sum([0, -7, 2, 15, -11, 2], 2))
#
#
#
#
# time = O(n)
# space = O(n)
def pair_sum_2(list, target):
  complements = {}
  indices = {}
  for i in range(len(list)):
    x = complements.get(list[i], None) 
    if x == None:
      complements[target-list[i]] = list[i]
      indices[list[i]] = i
    else:
      return [indices[x], i]
  return None

print(pair_sum_2([4, 2, 8, 9, 6], 8))