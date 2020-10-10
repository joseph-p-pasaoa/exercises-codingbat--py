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



# DIFF21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
  diff21 = abs(n - 21)

  if n > 21:
    return diff21 * 2
  else:
    return diff21

# diff21(19) → 2	2	OK	
# diff21(10) → 11	11	OK	
# diff21(21) → 0	0	OK	
# diff21(22) → 2	2	OK	
# diff21(25) → 8	8	OK	
# diff21(30) → 18	18	OK	
# diff21(0) → 21	21	OK	
# diff21(1) → 20	20	OK	
# diff21(2) → 19	19	OK	
# diff21(-1) → 22	22	OK	
# diff21(-2) → 23	23	OK	
# diff21(50) → 58	58	OK



# PARROT_TROUBLE
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
  isTroubleTime = hour < 7 or hour > 20
  return talking and isTroubleTime

# parrot_trouble(True, 6) → True	True	OK	
# parrot_trouble(True, 7) → False	False	OK	
# parrot_trouble(False, 6) → False	False	OK	
# parrot_trouble(True, 21) → True	True	OK	
# parrot_trouble(False, 21) → False	False	OK	
# parrot_trouble(False, 20) → False	False	OK	
# parrot_trouble(True, 23) → True	True	OK	
# parrot_trouble(False, 23) → False	False	OK	
# parrot_trouble(True, 20) → False	False	OK	
# parrot_trouble(False, 12) → False	False	OK



# MAKES10
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
#
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  return (a + b == 10) or (a == 10) or (b == 10)

# makes10(9, 10) → True	True	OK	
# makes10(9, 9) → False	False	OK	
# makes10(1, 9) → True	True	OK	
# makes10(10, 1) → True	True	OK	
# makes10(10, 10) → True	True	OK	
# makes10(8, 2) → True	True	OK	
# makes10(8, 3) → False	False	OK	
# makes10(10, 42) → True	True	OK	
# makes10(12, -2) → True	True	OK



# NEAR_HUNDRED
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
  distFrom100 = abs(100 - n)
  distFrom200 = abs(200 - n)

  return (distFrom100 <= 10) or (distFrom200 <= 10)

# near_hundred(93) → True	True	OK	
# near_hundred(90) → True	True	OK	
# near_hundred(89) → False	False	OK	
# near_hundred(110) → True	True	OK	
# near_hundred(111) → False	False	OK	
# near_hundred(121) → False	False	OK	
# near_hundred(-101) → False	False	OK	
# near_hundred(-209) → False	False	OK	
# near_hundred(190) → True	True	OK	
# near_hundred(209) → True	True	OK	
# near_hundred(0) → False	False	OK	
# near_hundred(5) → False	False	OK	
# near_hundred(-50) → False	False	OK	
# near_hundred(191) → True	True	OK	
# near_hundred(189) → False	False	OK	
# near_hundred(200) → True	True	OK	
# near_hundred(210) → True	True	OK	
# near_hundred(211) → False	False	OK	
# near_hundred(290) → False	False	OK



