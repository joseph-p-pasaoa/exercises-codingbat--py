# LOGIC-1


# CIGAR_PARTY
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
#
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  elif is_weekend:
    return True
  else:
    return cigars <= 60

# cigar_party(30, False) → False	False	OK	
# cigar_party(50, False) → True	True	OK	
# cigar_party(70, True) → True	True	OK	
# cigar_party(30, True) → False	False	OK	
# cigar_party(50, True) → True	True	OK	
# cigar_party(60, False) → True	True	OK	
# cigar_party(61, False) → False	False	OK	
# cigar_party(40, False) → True	True	OK	
# cigar_party(39, False) → False	False	OK	
# cigar_party(40, True) → True	True	OK	
# cigar_party(39, True) → False	False	OK	
# other tests OK



# DATE_FASHION
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes.The result getting the table is encoded
# as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result
# is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no).
# Otherwise the result is 1 (maybe).
#
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
  if min(you, date) <= 2:
    return 0
  elif max(you, date) >= 8:
    return 2
  else:
    return 1

# date_fashion(5, 10) → 2	2	OK	
# date_fashion(5, 2) → 0	0	OK	
# date_fashion(5, 5) → 1	1	OK	
# date_fashion(3, 3) → 1	1	OK	
# date_fashion(10, 2) → 0	0	OK	
# date_fashion(2, 9) → 0	0	OK	
# date_fashion(9, 9) → 2	2	OK	
# date_fashion(10, 5) → 2	2	OK	
# date_fashion(2, 2) → 0	0	OK	
# date_fashion(3, 7) → 1	1	OK	
# date_fashion(2, 7) → 0	0	OK	
# date_fashion(6, 2) → 0	0	OK	
# other tests OK



# SQUIRREL_PLAY
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is
# between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given
# an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
#
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
  if temp < 60 or temp > 100:
    return False
  else:
    return is_summer or temp <= 90

# squirrel_play(70, False) → True	True	OK	
# squirrel_play(95, False) → False	False	OK	
# squirrel_play(95, True) → True	True	OK	
# squirrel_play(90, False) → True	True	OK	
# squirrel_play(90, True) → True	True	OK	
# squirrel_play(50, False) → False	False	OK	
# squirrel_play(50, True) → False	False	OK	
# squirrel_play(100, False) → False	False	OK	
# squirrel_play(100, True) → True	True	OK	
# squirrel_play(105, True) → False	False	OK	
# squirrel_play(59, False) → False	False	OK	
# squirrel_play(59, True) → False	False	OK	
# squirrel_play(60, False) → True	True	OK	
# other tests OK
