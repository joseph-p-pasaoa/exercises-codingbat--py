#LIST-1


import math


# FIRST_LAST6
# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.
#
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  return 6 in nums[:1] + nums[-1:]

# first_last6([1, 2, 6]) → True	True	OK	
# first_last6([6, 1, 2, 3]) → True	True	OK	
# first_last6([13, 6, 1, 2, 3]) → False	False	OK	
# first_last6([13, 6, 1, 2, 6]) → True	True	OK	
# first_last6([3, 2, 1]) → False	False	OK	
# first_last6([3, 6, 1]) → False	False	OK	
# first_last6([3, 6]) → True	True	OK	
# first_last6([6]) → True	True	OK	
# first_last6([3]) → False	False	OK	
# first_last6([5, 6]) → True	True	OK	
# first_last6([5, 5]) → False	False	OK	
# first_last6([1, 2, 3, 4, 6]) → True	True	OK	
# first_last6([1, 2, 3, 4]) → False	False	OK	
# other tests OK



# SAME_FIRST_LAST
# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
#
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
  return len(nums) >= 1 and nums[:1] == nums[-1:]

# same_first_last([1, 2, 3]) → False	False	OK	
# same_first_last([1, 2, 3, 1]) → True	True	OK	
# same_first_last([1, 2, 1]) → True	True	OK	
# same_first_last([7]) → True	True	OK	
# same_first_last([]) → False	False	OK	
# same_first_last([1, 2, 3, 4, 5, 1]) → True	True	OK	
# same_first_last([1, 2, 3, 4, 5, 13]) → False	False	OK	
# same_first_last([13, 2, 3, 4, 5, 13]) → True	True	OK	
# same_first_last([7, 7]) → True	True	OK	
# other tests OK



# MAKE_PI
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
#
# make_pi() → [3, 1, 4]

def make_pi():
  pi = '{:.3f}'.format(math.pi)
  digits = ''.join(filter(lambda x : x.isdigit(), pi))
  first_three = [int(char) for char in digits[:3]]
  return first_three

# make_pi() → [3, 1, 4]	[3, 1, 4]	OK



