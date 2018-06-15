# We have a module called fibo which contains the following lines.

# Fibonacci numbers module
# see https://docs.python.org/2/tutorial/modules.html


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


import fibo

print dir(fibo)
# ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'fib', 'fib2']

print fibo.fib(1000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

print fibo.fib(100)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print fibo.__name__
# 'fibo'

fib = fibo.fib
print fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377

reload(fibo)
import fibo as fib
print fib.fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377

reload(fibo)
from fibo import fib as fibonacci
print fibonacci(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# would not encourage this usage
reload(fibo)
from fibo import *
print fib2(500)
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
