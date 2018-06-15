s = 'Hello World.'
str(s)
#'Hello World'
repr(s)
#"'Hello World.'"
str(1.0/7.0)
# '0.142857142857'
repr(1.0/7.0)
# '0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s
# The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print hellos
#'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
#"(32.5, 40000, ('spam', 'eggs'))"

# Here are three ways to write a table of squares and cubes:

for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)
# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
# 10 100 1000
for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
# 10 100 1000
for x in range(1, 11):
    print '%2d %3d %4d' % (x, x*x, x*x*x)
# 1   1    1
# 2   4    8
# 3   9   27
# 4  16   64
# 5  25  125
# 6  36  216
# 7  49  343
# 8  64  512
# 9  81  729
# 10 100 1000

'12'.zfill(5)  # '%05d' % 12
# '00012'
'-3.14'.zfill(7)  # '%07.2f' % -3.14
# '-003.14'%
'3.14159265359'.zfill(5)  # '%05.11f' % 3.14159265359
# '3.14159265359'
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
# We are the knights who say "Ni!"
print 'We who say "{1}" are the {0}!'.format('knights', 'Ni')
# We who say "Ni" are the knights!

print 'This {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible')
# This spam is absolutely horrible.

print 'The story of {0}, {1}, and {other} {other} {other}.'.format('Bill', 'Manfred',
                                                                   other='Georg')
# The story of Bill, Manfred, and Georg Georg Georg.

import math
print 'The value of PI is approximately {}.'.format(math.pi)
# The value of PI is approximately 3.14159265359.
print 'The value of PI is approximately {!r}.'.format(math.pi)
# The value of PI is approximately 3.141592653589793.
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
# The value of PI is approximately 3.142.

table = {'Peter': 4127, 'Paul': 4098, 'Mary': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
# Paul       ==>       4098
# Mary       ==>       7678
# Peter      ==>       4127

print ('Peter: {0[Peter]:d}; Paul: {0[Paul]:d}; '
       'Mary: {0[Mary]:d}'.format(table))
# Peter: 4127; Paul: 4098; Mary: 7678
print 'Peter: {Peter:d}; Paul: {Paul:d}; Mary: {Mary:d}'.format(**table)
# Peter: 4127; Paul: 4098; Mary: 7678
