import numpy as np


def add_intercept(x):
    """Adds a column of 1’s to the non-empty numpy.array x.
Args:
    x: has to be a non-empty 2-dimensional numpy.array, of shape (m, n).
Returns:
    x as a numpy.array, of shape (m, n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
Raises:
    This function should not raise any Exception.
"""
    if not isinstance(x, np.ndarray) or x.ndim != 2 or not x.size\
            or not np.issubdtype(x.dtype, np.number):
        print("x has to be a non-empty 2-dimensional numpy.array.")
        return None
    return np.concatenate((np.ones((x.shape[0], 1)), x), axis=1)
