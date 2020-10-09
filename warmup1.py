# WARMUP-1


# SLEEP_IN
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  return not weekday or vacation

# sleep_in(False, False) → True	True	OK	
# sleep_in(True, False) → False	False	OK	
# sleep_in(False, True) → True	True	OK	
# sleep_in(True, True) → True	True	OK	



# MONKEY_TROUBLE
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  return (a_smile == b_smile)

# monkey_trouble(True, True) → True	True	OK	
# monkey_trouble(False, False) → True	True	OK	
# monkey_trouble(True, False) → False	False	OK	
# monkey_trouble(False, True) → False	False	OK



# SUM_DOUBLE
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
  return (a + b) * 2 if (a == b) else (a + b)

# sum_double(1, 2) → 3	3	OK	
# sum_double(3, 2) → 5	5	OK	
# sum_double(2, 2) → 8	8	OK	
# sum_double(-1, 0) → -1	-1	OK	
# sum_double(3, 3) → 12	12	OK	
# sum_double(0, 0) → 0	0	OK	
# sum_double(0, 1) → 1	1	OK	
# sum_double(3, 4) → 7	7	OK



