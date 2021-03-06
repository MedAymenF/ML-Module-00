#!/usr/bin/env python3
import numpy as np


def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array,\
 without any for loop.
 The two arrays must have the same dimensions.
Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
Returns:
    The half mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.array.
    None if y and y_hat does not share the same dimensions.
    None if y or y_hat is not of the expected type.
Raises:
    This function should not raise any Exception.
"""
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.shape[1] != 1\
            or not y.size or not np.issubdtype(y.dtype, np.number):
        print("y has to be an numpy.array, a vector.")
        return None
    if not isinstance(y_hat, np.ndarray) or y_hat.ndim != 2 or\
            y_hat.shape[1] != 1 or not y_hat.size or\
            not np.issubdtype(y_hat.dtype, np.number):
        print("y_hat has to be an numpy.array, a vector.")
        return None
    error = y - y_hat
    return float(error.T.dot(error)[0, 0] / (2 * y.shape[0]))
