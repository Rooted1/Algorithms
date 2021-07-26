# given a list of string characters, return a list of indices that matches the target element
# input - list and target
# output - list of indices that matches target


def search(list, target):
  if not list:
    return None
  matches = []
  for i in range(len(list)):
    if list[i] == target:
      matches.append(i)
  if matches:
    return matches
  return None


print(search(['s', 'w', 'e', 'e', 't'], 'e'))
print(search([], 'e'))