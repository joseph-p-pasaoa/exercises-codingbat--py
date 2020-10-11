# WARMUP-2


# STRING_TIMES
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(str, n):
  output = ''
  for _ in range(n):
    output += str
  return output

# string_times('Hi', 2) → 'HiHi'	'HiHi'	OK	
# string_times('Hi', 3) → 'HiHiHi'	'HiHiHi'	OK	
# string_times('Hi', 1) → 'Hi'	'Hi'	OK	
# string_times('Hi', 0) → ''	''	OK	
# string_times('Hi', 5) → 'HiHiHiHiHi'	'HiHiHiHiHi'	OK	
# string_times('Oh Boy!', 2) → 'Oh Boy!Oh Boy!'	'Oh Boy!Oh Boy!'	OK	
# string_times('x', 4) → 'xxxx'	'xxxx'	OK	
# string_times('', 4) → ''	''	OK	
# string_times('code', 2) → 'codecode'	'codecode'	OK	
# string_times('code', 3) → 'codecodecode'	'codecodecode'	OK



# FRONT_TIMES
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  front_slice = str[:3]
  output = ''
  for _ in range(n):
    output += front_slice
  return output

# front_times('Chocolate', 2) → 'ChoCho'	'ChoCho'	OK	
# front_times('Chocolate', 3) → 'ChoChoCho'	'ChoChoCho'	OK	
# front_times('Abc', 3) → 'AbcAbcAbc'	'AbcAbcAbc'	OK	
# front_times('Ab', 4) → 'AbAbAbAb'	'AbAbAbAb'	OK	
# front_times('A', 4) → 'AAAA'	'AAAA'	OK	
# front_times('', 4) → ''	''	OK	
# front_times('Abc', 0) → ''	''	OK



# STRING_BITS
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
  return str[::2]

# string_bits('Hello') → 'Hlo'	'Hlo'	OK	
# string_bits('Hi') → 'H'	'H'	OK	
# string_bits('Heeololeo') → 'Hello'	'Hello'	OK	
# string_bits('HiHiHi') → 'HHH'	'HHH'	OK	
# string_bits('') → ''	''	OK	
# string_bits('Greetings') → 'Getns'	'Getns'	OK	
# string_bits('Chocoate') → 'Coot'	'Coot'	OK	
# string_bits('pi') → 'p'	'p'	OK	
# string_bits('Hello Kitten') → 'HloKte'	'HloKte'	OK	
# string_bits('hxaxpxpxy') → 'happy'	'happy'	OK



# STRING_SPLOSION
# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  output = ''
  for i in range(len(str)):
    output += str[:i + 1]
  return output

# string_splosion('Code') → 'CCoCodCode'	'CCoCodCode'	OK	
# string_splosion('abc') → 'aababc'	'aababc'	OK	
# string_splosion('ab') → 'aab'	'aab'	OK	
# string_splosion('x') → 'x'	'x'	OK	
# string_splosion('fade') → 'ffafadfade'	'ffafadfade'	OK	
# string_splosion('There') → 'TThTheTherThere'	'TThTheTherThere'	OK	
# string_splosion('Kitten') → 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
# string_splosion('Bye') → 'BByBye'	'BByBye'	OK	
# string_splosion('Good') → 'GGoGooGood'	'GGoGooGood'	OK	
# string_splosion('Bad') → 'BBaBad'	'BBaBad'	OK



