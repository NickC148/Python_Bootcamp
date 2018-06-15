x = 3
if x == 1:
    print 'x is 1'
elif x == 2:
    pass
elif x == 3:
    print "Hello There"
else:
    print x
# Hello There​

# Python equivalent of the C :- y = x == 3 ? 4 : 5;

y = 4 if x == 3 else 5

a = 1
b = 2
c = 3
d = 4


if a == 1 and b == 2 and c == 3 and d == 4:
    print 'as above'
    # as above

# You can set data with tuple syntax
a, b, c, d = 1, 2, 3, 4

if a < c < d:
    print True
    # True

# Comparing Sequences and Other Types
print '''\
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
'''
#(1, 2, 3)              < (1, 2, 4)
#[1, 2, 3]              < [1, 2, 4]
#'ABC' < 'C' < 'Pascal' < 'Python'
#(1, 2, 3, 4)           < (1, 2, 4)
#(1, 2)                 < (1, 2, -1)
#(1, 2, 3)             == (1.0, 2.0, 3.0)
#(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

xx = (1, 2, 3) < (1, 2, 4)
print xx
# True
xx = [1, 2, 3] < [1, 2, 4]
print xx
# True
xx = 'ABC' < 'C' < 'Pascal' < 'Python'
print xx
# True
xx = (1, 2, 3, 4) < (1, 2, 4)
print xx
# True
xx = (1, 2) < (1, 2, -1)
print xx
# True
xx = (1, 2, 3) == (1.0, 2.0, 3.0)
print xx
# True
xx = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
print xx
# True
