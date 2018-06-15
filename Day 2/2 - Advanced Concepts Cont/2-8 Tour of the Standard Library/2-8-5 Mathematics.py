### 2-8-5 Mathematics ###
# The math module gives access to the underlying C library functions for floating point math.

import math
math.cos(math.pi / 4.0)
# 0.7071067811865476
math.log(1024, 2)
# 10

# The random module provides tools for making random selections.

import random
alist = ['banana', 'apple', 'blackberry']
random.choice(alist)
random.random()
random.randrange(6)
