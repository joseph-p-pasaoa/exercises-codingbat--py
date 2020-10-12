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
