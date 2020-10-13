# LOGIC-2


import math


# MAKE_BRICKS
# We want to make a row of bricks that is goal inches long. We have a number of small bricks
# (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal
# by choosing from the given bricks. This is a little harder than it looks and can be done
# without any loops. See also: Introduction to MakeBricks
#
# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  max_bigs_wanted = math.floor(goal / 5)

  bigs_applied = min(big, max_bigs_wanted)
  smalls_needed = goal - bigs_applied * 5

  return small >= smalls_needed

# make_bricks(3, 1, 8) → True	True	OK	
# make_bricks(3, 1, 9) → False	False	OK	
# make_bricks(3, 2, 10) → True	True	OK	
# make_bricks(3, 2, 8) → True	True	OK	
# make_bricks(3, 2, 9) → False	False	OK	
# make_bricks(6, 1, 11) → True	True	OK	
# make_bricks(6, 0, 11) → False	False	OK	
# make_bricks(1, 4, 11) → True	True	OK	
# make_bricks(0, 3, 10) → True	True	OK	
# make_bricks(1, 4, 12) → False	False	OK	
# make_bricks(3, 1, 7) → True	True	OK	
# make_bricks(1, 1, 7) → False	False	OK	
# make_bricks(2, 1, 7) → True	True	OK	
# make_bricks(7, 1, 11) → True	True	OK	
# make_bricks(7, 1, 8) → True	True	OK	
# make_bricks(7, 1, 13) → False	False	OK	
# make_bricks(43, 1, 46) → True	True	OK	
# make_bricks(40, 1, 46) → False	False	OK	
# make_bricks(40, 2, 47) → True	True	OK	
# make_bricks(40, 2, 50) → True	True	OK	
# make_bricks(40, 2, 52) → False	False	OK	
# make_bricks(22, 2, 33) → False	False	OK	
# make_bricks(0, 2, 10) → True	True	OK	
# make_bricks(1000000, 1000, 1000100) → True	True	OK	
# make_bricks(2, 1000000, 100003) → False	False	OK	
# make_bricks(20, 0, 19) → True	True	OK	
# make_bricks(20, 0, 21) → False	False	OK	
# make_bricks(20, 4, 51) → False	False	OK	
# make_bricks(20, 4, 39) → True	True	OK	
# other tests OK



# LONE_SUM
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as
# another of the values, it does not count towards the sum.
#
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
  sum = 0
  seen = {}
  for num in [a, b, c]:
    if not num in seen:
      seen[num] = 1
    else:
      seen[num] = seen[num] + 1
  for num, count in seen.items():
    if count == 1:
      sum += num

  return sum

# lone_sum(1, 2, 3) → 6	6	OK	
# lone_sum(3, 2, 3) → 2	2	OK	
# lone_sum(3, 3, 3) → 0	0	OK	
# lone_sum(9, 2, 2) → 9	9	OK	
# lone_sum(2, 2, 9) → 9	9	OK	
# lone_sum(2, 9, 2) → 9	9	OK	
# lone_sum(2, 9, 3) → 14	14	OK	
# lone_sum(4, 2, 3) → 9	9	OK	
# lone_sum(1, 3, 1) → 3	3	OK	
# other tests OK



# LUCKY_SUM
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not
# count towards the sum and values to its right do not count. So for example, if b is 13, then
# both b and c do not count.
#
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
  sum = 0
  for num in [a, b, c]:
    if num == 13:
      break
    else:
      sum += num

  return sum

# lucky_sum(1, 2, 3) → 6	6	OK	
# lucky_sum(1, 2, 13) → 3	3	OK	
# lucky_sum(1, 13, 3) → 1	1	OK	
# lucky_sum(1, 13, 13) → 1	1	OK	
# lucky_sum(6, 5, 2) → 13	13	OK	
# lucky_sum(13, 2, 3) → 0	0	OK	
# lucky_sum(13, 2, 13) → 0	0	OK	
# lucky_sum(13, 13, 2) → 0	0	OK	
# lucky_sum(9, 4, 13) → 13	13	OK	
# lucky_sum(8, 13, 2) → 8	8	OK	
# lucky_sum(7, 2, 1) → 10	10	OK	
# lucky_sum(3, 3, 13) → 6	6	OK	
# other tests OK



# NO_TEEN_SUM
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in
# the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as
# a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that
# value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times
# (i.e. "decomposition"). Define the helper below and at the same indent level as the main
# no_teen_sum().
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  sum = 0
  for num in [a, b, c]:
    sum += fix_teen(num)

  return sum


def fix_teen(n):
  if n in [15, 16]:
    return n
  elif n >= 13 and n <= 19:
    return 0
  else:
    return n

# no_teen_sum(1, 2, 3) → 6	6	OK	
# no_teen_sum(2, 13, 1) → 3	3	OK	
# no_teen_sum(2, 1, 14) → 3	3	OK	
# no_teen_sum(2, 1, 15) → 18	18	OK	
# no_teen_sum(2, 1, 16) → 19	19	OK	
# no_teen_sum(2, 1, 17) → 3	3	OK	
# no_teen_sum(17, 1, 2) → 3	3	OK	
# no_teen_sum(2, 15, 2) → 19	19	OK	
# no_teen_sum(16, 17, 18) → 16	16	OK	
# no_teen_sum(17, 18, 19) → 0	0	OK	
# no_teen_sum(15, 16, 1) → 32	32	OK	
# no_teen_sum(15, 15, 19) → 30	30	OK	
# no_teen_sum(15, 19, 16) → 31	31	OK	
# no_teen_sum(5, 17, 18) → 5	5	OK	
# no_teen_sum(17, 18, 16) → 16	16	OK	
# no_teen_sum(17, 19, 18) → 0	0	OK	
# other tests OK



# ROUND_SUM
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is
# 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its
# rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of
# their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call
# it 3 times. Write the helper entirely below and at the same indent level as round_sum().
#
# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
  sum = 0
  for num in [a, b, c]:
    sum += round10(num)

  return sum


def round10(num):
  num = float(num)

  if num % 10 < 5:
    return int(math.floor(num / 10) * 10)
  else:
    return int(math.ceil(num / 10) * 10)

# round_sum(16, 17, 18) → 60	60	OK	
# round_sum(12, 13, 14) → 30	30	OK	
# round_sum(6, 4, 4) → 10	10	OK	
# round_sum(4, 6, 5) → 20	20	OK	
# round_sum(4, 4, 6) → 10	10	OK	
# round_sum(9, 4, 4) → 10	10	OK	
# round_sum(0, 0, 1) → 0	0	OK	
# round_sum(0, 9, 0) → 10	10	OK	
# round_sum(10, 10, 19) → 40	40	OK	
# round_sum(20, 30, 40) → 90	90	OK	
# round_sum(45, 21, 30) → 100	100	OK	
# round_sum(23, 11, 26) → 60	60	OK	
# round_sum(23, 24, 25) → 70	70	OK	
# round_sum(25, 24, 25) → 80	80	OK	
# round_sum(23, 24, 29) → 70	70	OK	
# round_sum(11, 24, 36) → 70	70	OK	
# round_sum(24, 36, 32) → 90	90	OK	
# round_sum(14, 12, 26) → 50	50	OK	
# round_sum(12, 10, 24) → 40	40	OK	
# other tests OK



# CLOSE_FAR
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes
# the absolute value of a number.
#
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
  ab_diff = abs(a - b)
  ac_diff = abs(a - c)
  bc_diff = abs(b - c)
  
  if (ab_diff <= 1 and ac_diff >= 2):
    return bc_diff >= 2  
  elif (ab_diff >= 2 and ac_diff <= 1):
    return bc_diff >= 2
  else:
    return False

# close_far(1, 2, 10) → True	True	OK	
# close_far(1, 2, 3) → False	False	OK	
# close_far(4, 1, 3) → True	True	OK	
# close_far(4, 5, 3) → False	False	OK	
# close_far(4, 3, 5) → False	False	OK	
# close_far(-1, 10, 0) → True	True	OK	
# close_far(0, -1, 10) → True	True	OK	
# close_far(10, 10, 8) → True	True	OK	
# close_far(10, 8, 9) → False	False	OK	
# close_far(8, 9, 10) → False	False	OK	
# close_far(8, 9, 7) → False	False	OK	
# close_far(8, 6, 9) → True	True	OK	
# other tests OK



# MAKE_CHOCOLATE
# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars
# (5 kilos each). Return the number of small bars to use, assuming we always use big bars before
# small bars. Return -1 if it can't be done.
#
# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
  max_big_wanted = math.floor(goal / 5)
  
  bigs_applied = min(max_big_wanted, big)
  smalls_needed = goal - bigs_applied * 5
  
  if small >= smalls_needed:
    return int(min(small, smalls_needed))
  else:
    return -1

# make_chocolate(4, 1, 9) → 4	4	OK	
# make_chocolate(4, 1, 10) → -1	-1	OK	
# make_chocolate(4, 1, 7) → 2	2	OK	
# make_chocolate(6, 2, 7) → 2	2	OK	
# make_chocolate(4, 1, 5) → 0	0	OK	
# make_chocolate(4, 1, 4) → 4	4	OK	
# make_chocolate(5, 4, 9) → 4	4	OK	
# make_chocolate(9, 3, 18) → 3	3	OK	
# make_chocolate(3, 1, 9) → -1	-1	OK	
# make_chocolate(1, 2, 7) → -1	-1	OK	
# make_chocolate(1, 2, 6) → 1	1	OK	
# make_chocolate(1, 2, 5) → 0	0	OK	
# make_chocolate(6, 1, 10) → 5	5	OK	
# make_chocolate(6, 1, 11) → 6	6	OK	
# make_chocolate(6, 1, 12) → -1	-1	OK	
# make_chocolate(6, 1, 13) → -1	-1	OK	
# make_chocolate(6, 2, 10) → 0	0	OK	
# make_chocolate(6, 2, 11) → 1	1	OK	
# make_chocolate(6, 2, 12) → 2	2	OK	
# make_chocolate(60, 100, 550) → 50	50	OK	
# make_chocolate(1000, 1000000, 5000006) → 6	6	OK	
# make_chocolate(7, 1, 12) → 7	7	OK	
# make_chocolate(7, 1, 13) → -1	-1	OK	
# make_chocolate(7, 2, 13) → 3	3	OK	
# other tests OK
