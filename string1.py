# STRING-1


# HELLO_NAME
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
  return 'Hello {}!'.format(name)

# hello_name('Bob') → 'Hello Bob!'	'Hello Bob!'	OK	
# hello_name('Alice') → 'Hello Alice!'	'Hello Alice!'	OK	
# hello_name('X') → 'Hello X!'	'Hello X!'	OK	
# hello_name('Dolly') → 'Hello Dolly!'	'Hello Dolly!'	OK	
# hello_name('Alpha') → 'Hello Alpha!'	'Hello Alpha!'	OK	
# hello_name('Omega') → 'Hello Omega!'	'Hello Omega!'	OK	
# hello_name('Goodbye') → 'Hello Goodbye!'	'Hello Goodbye!'	OK	
# hello_name('ho ho ho') → 'Hello ho ho ho!'	'Hello ho ho ho!'	OK	
# hello_name('xyz!') → 'Hello xyz!!'	'Hello xyz!!'	OK	
# hello_name('Hello') → 'Hello Hello!'	'Hello Hello!'	OK	
# other tests OK



# MAKE_ABBA
# Given two strings, a and b, return the result of putting them together in the order abba,
# e.g. "Hi" and "Bye" returns "HiByeByeHi".
#
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
  return ''.join([a, b, b, a])

# make_abba('Hi', 'Bye') → 'HiByeByeHi'	'HiByeByeHi'	OK	
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'	'YoAliceAliceYo'	OK	
# make_abba('What', 'Up') → 'WhatUpUpWhat'	'WhatUpUpWhat'	OK	
# make_abba('aaa', 'bbb') → 'aaabbbbbbaaa'	'aaabbbbbbaaa'	OK	
# make_abba('x', 'y') → 'xyyx'	'xyyx'	OK	
# make_abba('x', '') → 'xx'	'xx'	OK	
# make_abba('', 'y') → 'yy'	'yy'	OK	
# make_abba('Bo', 'Ya') → 'BoYaYaBo'	'BoYaYaBo'	OK	
# make_abba('Ya', 'Ya') → 'YaYaYaYa'	'YaYaYaYa'	OK	
# other tests OK



# MAKE_TAGS
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example,
# the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the
# HTML string with tags around the word, e.g. "<i>Yay</i>".
#
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
  return '<{0}>{1}</{0}>'.format(tag, word)

# ake_tags('i', 'Yay') → '<i>Yay</i>'	'<i>Yay</i>'	OK	
# make_tags('i', 'Hello') → '<i>Hello</i>'	'<i>Hello</i>'	OK	
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'	'<cite>Yay</cite>'	OK	
# make_tags('address', 'here') → '<address>here</address>'	'<address>here</address>'	OK	
# make_tags('body', 'Heart') → '<body>Heart</body>'	'<body>Heart</body>'	OK	
# make_tags('i', 'i') → '<i>i</i>'	'<i>i</i>'	OK	
# make_tags('i', '') → '<i></i>'	'<i></i>'	OK	
# other tests OK



