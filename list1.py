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



# COMMON_END
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
#
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

# common_end([1, 2, 3], [7, 3]) → True	True	OK	
# common_end([1, 2, 3], [7, 3, 2]) → False	False	OK	
# common_end([1, 2, 3], [1, 3]) → True	True	OK	
# common_end([1, 2, 3], [1]) → True	True	OK	
# common_end([1, 2, 3], [2]) → False	False	OK	
# other tests OK



# SUM3
# Given an array of ints length 3, return the sum of all the elements.
#
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(nums):
  return sum(nums)

# sum3([1, 2, 3]) → 6	6	OK	
# sum3([5, 11, 2]) → 18	18	OK	
# sum3([7, 0, 0]) → 7	7	OK	
# sum3([1, 2, 1]) → 4	4	OK	
# sum3([1, 1, 1]) → 3	3	OK	
# sum3([2, 7, 2]) → 11	11	OK



# ROTATE_LEFT3
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  return nums[1:] + nums[:1]

# rotate_left3([1, 2, 3]) → [2, 3, 1]	[2, 3, 1]	OK	
# rotate_left3([5, 11, 9]) → [11, 9, 5]	[11, 9, 5]	OK	
# rotate_left3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK	
# rotate_left3([1, 2, 1]) → [2, 1, 1]	[2, 1, 1]	OK	
# rotate_left3([0, 0, 1]) → [0, 1, 0]	[0, 1, 0]	OK	
# other tests OK



# REVERSE3
# Given an array of ints length 3, return a new array with the elements in reverse order,
# so {1, 2, 3} becomes {3, 2, 1}.
#
# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  return nums[::-1]

# reverse3([1, 2, 3]) → [3, 2, 1]	[3, 2, 1]	OK	
# reverse3([5, 11, 9]) → [9, 11, 5]	[9, 11, 5]	OK	
# reverse3([7, 0, 0]) → [0, 0, 7]	[0, 0, 7]	OK	
# reverse3([2, 1, 2]) → [2, 1, 2]	[2, 1, 2]	OK	
# reverse3([1, 2, 1]) → [1, 2, 1]	[1, 2, 1]	OK	
# reverse3([2, 11, 3]) → [3, 11, 2]	[3, 11, 2]	OK	
# reverse3([0, 6, 5]) → [5, 6, 0]	[5, 6, 0]	OK	
# reverse3([7, 2, 3]) → [3, 2, 7]	[3, 2, 7]	OK	
# other tests OK 


