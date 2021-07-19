# given a string return True if the string is palindrome or False if it's not

# Recursive solution
def palindrome_1(str):
  if len(str) <= 1:
    return True

  lower_str = str.lower()
  punc_and_space = ['.', ',', '?', '!', ' ']
  no_punc_str = lower_str[:]

  for punc in punc_and_space:
    no_punc_str = no_punc_str.replace(punc, '')

  if no_punc_str[0] != no_punc_str[-1]:
    return False
  return palindrome_1(no_punc_str[1:-1])

print(palindrome_1("aboa"))
print(palindrome_1("racecar"))
print(palindrome_1("Aba"))
print(palindrome_1("Racecar!"))
print(palindrome_1("Taco Cat!"))
#
#
#
#
#
#
#
#
#
# iterative solution
def palindrome_2(str):
  if len(str) <= 1:
    return True
  lower_str = str.lower()
  punc_and_space = ['.', ',', '?', '!', ' ']
  no_punc_str = lower_str[:]

  for punc in punc_and_space:
    no_punc_str = no_punc_str.replace(punc, '')
  for i in range(len(no_punc_str) // 2):
    if no_punc_str[i] != no_punc_str[-i-1]:
      return False
  return True

print(palindrome_2("Racecar!"))
print(palindrome_2("Taco Cat!"))
print(palindrome_2("aboa !"))
print(palindrome_2("!"))