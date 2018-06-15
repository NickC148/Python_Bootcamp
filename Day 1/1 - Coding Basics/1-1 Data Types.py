# ----------------------------------------
# int, long, float, string, boolean, None
# ----------------------------------------

i = 4
l = 12l
f = 1.2
s = 'xyz'
n = i + l

print i, l, f, s, n
# 4 12 1.2 xyz 16

s2 = s + str(f)

print s2
# xyz1.2

print type(i), type(l), type(f), type(s), type(n), type(s2)
# <type 'int'> <type 'long'> <type 'float'> <type 'str'> <type 'long'> <type 'str'>

print """i:%s
l:%s
f:%s
s:%s
n:%s
s2:%s""" % (type(i), type(l), type(f), type(s), type(n), type(s2))
# i:<type 'int'>
# l:<type 'long'>
# f:<type 'float'>
# s:<type 'str'>
# n:<type 'long'>
# s2:<type 'str'>

s3 = '%s --- %s -- %d - %ld %f' % (s, s2, i, l, f)

print s3
# xyz --- xyz1.2 -- 4 - 12 1.200000

xt = True
xf = False
xn = None

print xt, xf, xn
# True False None
print repr(xt), repr(xf), repr(xn)
# True False None
print `xt`, `xf`, `xn`, `i`, `s`
# True False None 4 'xyz'
