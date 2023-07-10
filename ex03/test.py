#!/usr/bin/env python3
import numpy as np
from tools import add_intercept
# Example 1:
x = np.arange(1, 6).reshape((5, 1))
print(repr(add_intercept(x)))
# Output:
'''
array([[1., 1.],
       [1., 2.],
       [1., 3.],
       [1., 4.],
       [1., 5.]])
'''
# Example 2:
y = np.arange(1, 10).reshape((3, 3))
print(repr(add_intercept(y)))
# Output:
'''
array([[1., 1., 2., 3.],
       [1., 4., 5., 6.],
       [1., 7., 8., 9.]])
'''
