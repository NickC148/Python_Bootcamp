def fibonacci_looped(to_max):
    a, b = 0, 1
    while b < to_max:
        print b,
    a, b = b, a+b
    print


fibonacci_looped(40000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657


def fiboeven(to_max):
    sum_of = 0
    p1 = 0
    p2 = 1
    p3 = p1 + p2
    while sum_of + p1 < to_max:
        print p1, p2, p3,
        sum_of += p1
        p1 = p2 + p3
        p2 = p3 + p1
        p3 = p1 + p2
    print
    print 'sum of evens', sum_of


fiboeven(40000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657
# sum of evens 14328


def make_multiplier(n):
    def func(x):
        return x*n
    return func


t4 = make_multiplier(4)
t5 = make_multiplier(5)

print 't4(11)*t5(17)', t4(11)*t5(17)
# t4(11)*t5(17) 3740


def make_multiplier2(n):
    return lambda x: x * n


t4 = make_multiplier2(4)
t5 = make_multiplier2(5)

print 't4(11)*t5(17)', t4(11)*t5(17)
# t4(11)*t5(17) 3740

print '''\
Beware that default parameters are evaluated once
def f(a, L=[]):
 L.append(a)
 return L
'''
# Beware that default parameters are evaluated once
# def f(a, L=[]):
# L.append(a)
# return L


def f(a, L=[]):
    L.append(a)
    return L


print 'f(1)', f(1)
#f(1) [1]
print 'f(2)', f(2)
#f(2) [1, 2]
print 'f(3)', f(3)
#f(3) [1, 2, 3]


def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]


for char in reverse('pomelo'):
    print char
# o
# l
# e
# m
# o
# p
