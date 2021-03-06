### 2-8-9 Performance Measurement ###
# Some Python users develop a deep interest in knowing the relative performance of different approaches
# to the same problem. Python provides a measurement tool that answers those questions immediately.

# For example, it may be tempting to use the tuple packing and unpacking feature instead of the
# traditional approach to swapping arguments. The timeit module quickly demonstrates a modest
# performance advantage.

from timeit import Timer
print Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.0320846332396
print Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.026504411628

# In contrast to timeit‘s fine level of granularity, the profile and pstats modules provide tools for
# identifying time critical sections in larger blocks of code.
