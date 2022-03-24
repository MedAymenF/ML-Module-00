import numpy as np


def loss_elem_(y, y_hat):
    """Description:
    Calculates all the elements (y_pred - y)^2 of the loss function.
Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
Returns:
    J_elem: numpy.array, a vector of dimension\
 (number of the training examples,1).
    None if there is a dimension matching problem between y and y_hat.
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
    if y.shape[0] != y_hat.shape[0]:
        print('y and y_hat have different shapes')
        return None
    return (y - y_hat) ** 2


def loss_(y, y_hat):
    """Description:
    Calculates the value of loss function.
Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
Returns:
    J_value : has to be a float.
    None if there is a shape matching problem between y or y_hat.
    None if y or y_hat is not of the expected type.
Raises:
    This function should not raise any Exception.
"""
    squared_error = loss_elem_(y, y_hat)
    if squared_error is None:
        return None
    return squared_error.sum() / (2 * y.shape[0])
