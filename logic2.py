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



