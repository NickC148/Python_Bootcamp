# Lists are mutable vectors of zero or more elements and elements in a list can be
# added, change or removed. They are denoted using square brackets. Tuples are
# immutable vectors which cannot be modified. They are denoted using parenthesis
# (round brackets). Strings are immutable so that individual characters cannot be
# changed, the whole string must be replaced for changes.

squares = [1, 4, 9, 16, 25]
print squares
[1, 4, 9, 16, 25]

print squares[0], '# first element'
# 1 # first element
print squares[-1], '# last element'
# 25 # last element
print squares[1:2], '# new list of second element'
# [4] # new list of second element
print squares[-3:], '# new list of last three elements'
# [9, 16, 25] # new list of last three elements
print squares[:3], '# new list of first three elements'
# [1, 4, 9] # new list of first three elements

big_squares = squares + [36, 49, 64, 81, 100]
print big_squares
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print 4 ** 3  # the cube of 4 is 64, not 65!
# 64
cubes[3] = 4 ** 3
print cubes
#[1, 8, 27, 64, 125]
cubes.append(6 ** 3)
cubes.append(7 ** 3)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print letters
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print letters
#['a', 'b', 'C', 'D', 'E', 'f', 'g']
letters[2:5] = []
print letters
#['a', 'b', 'f', 'g']
letters[:] = []
print letters
# []

letters = ['a', 'b', 'c', 'd']
print len(letters)
# 4

mixed = [squares, cubes, letters]
print mixed
#[[1, 4, 9, 16, 25], [1, 8, 27, 64, 125, 216, 343], ['a', 'b', 'c', 'd']]
print mixed[1]
#[1, 8, 27, 64, 125, 216, 343]
print mixed[0][3]
# 16
