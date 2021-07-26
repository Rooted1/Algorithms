# return duplicate counts


def search(list, target):
  if not list:
    return None
  count = {}
  idx = []
   
  for el in list:
    if el not in count :
      count[el] = 0
    count[el] += 1

  for i in target:
    if i in count:
      idx.append(count[i])
    else:
      idx.append(0)
  return idx


print(search(['s', 'w', 'e', 'e', 't'], ['e','r']))
# print(search([], 'e'))