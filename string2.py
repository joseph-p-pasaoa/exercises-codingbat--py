# STRING-2


# DOUBLE_CHAR
# Given a string, return a string where for every char in the original, there are two chars.
#
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
  output = ''
  for char in str:
    output += char * 2
  return output

# double_char('The') → 'TThhee'	'TThhee'	OK	
# double_char('AAbb') → 'AAAAbbbb'	'AAAAbbbb'	OK	
# double_char('Hi-There') → 'HHii--TThheerree'	'HHii--TThheerree'	OK	
# double_char('Word!') → 'WWoorrdd!!'	'WWoorrdd!!'	OK	
# double_char('!!') → '!!!!'	'!!!!'	OK	
# double_char('') → ''	''	OK	
# double_char('a') → 'aa'	'aa'	OK	
# double_char('.') → '..'	'..'	OK	
# double_char('aa') → 'aaaa'	'aaaa'	OK	
# other tests OK



# COUNT_HI
# Return the number of times that the string "hi" appears anywhere in the given string.
#
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
  counter = 0
  for i in range(len(str) - 1):
    if str[i:i + 2] == 'hi':
      counter += 1
  return counter

# count_hi('abc hi ho') → 1	1	OK	
# count_hi('ABChi hi') → 2	2	OK	
# count_hi('hihi') → 2	2	OK	
# count_hi('hiHIhi') → 2	2	OK	
# count_hi('') → 0	0	OK	
# count_hi('h') → 0	0	OK	
# count_hi('hi') → 1	1	OK	
# count_hi('Hi is no HI on ahI') → 0	0	OK	
# count_hi('hiho not HOHIhi') → 2	2	OK	
# other tests OK



# CAT_DOG
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
  balance = 0
  for i in range(len(str) - 2):
    slice = str[i:i + 3]
    if slice == 'cat':
      balance += 1
    elif slice == 'dog':
      balance -= 1

  return balance == 0

# cat_dog('catdog') → True	True	OK	
# cat_dog('catcat') → False	False	OK	
# cat_dog('1cat1cadodog') → True	True	OK	
# cat_dog('catxxdogxxxdog') → False	False	OK	
# cat_dog('catxdogxdogxcat') → True	True	OK	
# cat_dog('catxdogxdogxca') → False	False	OK	
# cat_dog('dogdogcat') → False	False	OK	
# cat_dog('dogogcat') → True	True	OK	
# cat_dog('dog') → False	False	OK	
# cat_dog('cat') → False	False	OK	
# cat_dog('ca') → True	True	OK	
# cat_dog('c') → True	True	OK	
# cat_dog('') → True	True	OK	
# other tests OK



# COUNT_CODE
# Return the number of times that the string "code" appears anywhere in the given string, except we'll
# accept any letter for the 'd', so "cope" and "cooe" count.
#
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
  counter = 0
  for i in range(len(str) - 3):
    if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
      counter += 1

  return counter

# count_code('aaacodebbb') → 1	1	OK	
# count_code('codexxcode') → 2	2	OK	
# count_code('cozexxcope') → 2	2	OK	
# count_code('cozfxxcope') → 1	1	OK	
# count_code('xxcozeyycop') → 1	1	OK	
# count_code('cozcop') → 0	0	OK	
# count_code('abcxyz') → 0	0	OK	
# count_code('code') → 1	1	OK	
# count_code('ode') → 0	0	OK	
# count_code('c') → 0	0	OK	
# count_code('') → 0	0	OK	
# count_code('AAcodeBBcoleCCccoreDD') → 3	3	OK	
# count_code('AAcodeBBcoleCCccorfDD') → 2	2	OK	
# count_code('coAcodeBcoleccoreDD') → 3	3	OK	
# other tests OK



# END_OTHER
# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
  short = a if len(a) < len(b) else b
  long = b if len(a) < len(b) else a

  is_at_end = long.lower().endswith(short.lower())

  return is_at_end

# end_other('Hiabc', 'abc') → True	True	OK	
# end_other('AbC', 'HiaBc') → True	True	OK	
# end_other('abc', 'abXabc') → True	True	OK	
# end_other('Hiabc', 'abcd') → False	False	OK	
# end_other('Hiabc', 'bc') → True	True	OK	
# end_other('Hiabcx', 'bc') → False	False	OK	
# end_other('abc', 'abc') → True	True	OK	
# end_other('xyz', '12xyz') → True	True	OK	
# end_other('yz', '12xz') → False	False	OK	
# end_other('Z', '12xz') → True	True	OK	
# end_other('12', '12') → True	True	OK	
# end_other('abcXYZ', 'abcDEF') → False	False	OK	
# end_other('ab', 'ab12') → False	False	OK	
# end_other('ab', '12ab') → True	True	OK	
# other tests OK



# XYZ_THERE
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly
# preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
  for i in range(len(str) - 2):
    if i == 0 and str[:3] == 'xyz':
      return True
    elif str[i + 1:i + 4] == 'xyz' and not str[i] == '.':
      return True

  return False

# xyz_there('abcxyz') → True	True	OK	
# xyz_there('abc.xyz') → False	False	OK	
# xyz_there('xyz.abc') → True	True	OK	
# xyz_there('abcxy') → False	False	OK	
# xyz_there('xyz') → True	True	OK	
# xyz_there('xy') → False	False	OK	
# xyz_there('x') → False	False	OK	
# xyz_there('') → False	False	OK	
# xyz_there('abc.xyzxyz') → True	True	OK	
# xyz_there('abc.xxyz') → True	True	OK	
# xyz_there('.xyz') → False	False	OK	
# xyz_there('12.xyz') → False	False	OK	
# xyz_there('12xyz') → True	True	OK	
# xyz_there('1.xyz.xyz2.xyz') → False	False	OK	
# other tests OK
