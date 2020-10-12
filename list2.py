# LIST-2


# COUNT_EVENS
# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder,
# e.g. 5 % 2 is 1.
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count += 1

  return count

# count_evens([2, 1, 2, 3, 4]) → 3	3	OK	
# count_evens([2, 2, 0]) → 3	3	OK	
# count_evens([1, 3, 5]) → 0	0	OK	
# count_evens([]) → 0	0	OK	
# count_evens([11, 9, 0, 1]) → 1	1	OK	
# count_evens([2, 11, 9, 0]) → 2	2	OK	
# count_evens([2]) → 1	1	OK	
# count_evens([2, 5, 12]) → 2	2	OK	
# other tests OK



# BIG_DIFF
# Given an array length 1 or more of ints, return the difference between the largest and smallest values
# in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or
# larger of two values.
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
  max, min = -float('inf'), float('inf')
  for num in nums:
    if num < min:
      min = num
    if num > max:
      max = num

  return max - min

# big_diff([10, 3, 5, 6]) → 7	7	OK	
# big_diff([7, 2, 10, 9]) → 8	8	OK	
# big_diff([2, 10, 7, 2]) → 8	8	OK	
# big_diff([2, 10]) → 8	8	OK	
# big_diff([10, 2]) → 8	8	OK	
# big_diff([10, 0]) → 10	10	OK	
# big_diff([2, 3]) → 1	1	OK	
# big_diff([2, 2]) → 0	0	OK	
# big_diff([2]) → 0	0	OK	
# big_diff([5, 1, 6, 1, 9, 9]) → 8	8	OK	
# big_diff([7, 6, 8, 5]) → 3	3	OK	
# big_diff([7, 7, 6, 8, 5, 5, 6]) → 3	3	OK	
# other tests OK



# CENTERED_AVERAGE
# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the
# smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce
# the final average. You may assume that the array is length 3 or more.
#
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  sum = 0
  min, max = float('inf'), -float('inf')
  for num in nums:
    sum += num
    if num < min:
      min = num
    if num > max:
      max = num

  centered_sum = sum - (min + max)
  centered_len = len(nums) - 2
  
  return centered_sum / centered_len

# centered_average([1, 2, 3, 4, 100]) → 3	3	OK	
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5	5	OK	
# centered_average([-10, -4, -2, -4, -2, 0]) → -3	-3	OK	
# centered_average([5, 3, 4, 6, 2]) → 4	4	OK	
# centered_average([5, 3, 4, 0, 100]) → 4	4	OK	
# centered_average([100, 0, 5, 3, 4]) → 4	4	OK	
# centered_average([4, 0, 100]) → 4	4	OK	
# centered_average([0, 2, 3, 4, 100]) → 3	3	OK	
# centered_average([1, 1, 100]) → 1	1	OK	
# centered_average([7, 7, 7]) → 7	7	OK	
# centered_average([1, 7, 8]) → 7	7	OK	
# centered_average([1, 1, 99, 99]) → 50	50	OK	
# centered_average([1000, 0, 1, 99]) → 50	50	OK	
# centered_average([4, 4, 4, 4, 5]) → 4	4	OK	
# centered_average([4, 4, 4, 1, 5]) → 4	4	OK	
# centered_average([6, 4, 8, 12, 3]) → 6	6	OK	
# other tests OK



