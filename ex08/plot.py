import matplotlib.pyplot as plt
import numpy as np


def plot_with_loss(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a vector of shape 2 * 1.
Returns:
    Nothing.
Raises:
    This function should not raise any Exception.
"""
    if not isinstance(x, np.ndarray) or x.ndim != 2 or x.shape[1] != 1\
            or not x.size or not np.issubdtype(x.dtype, np.number):
        print("x has to be an numpy.array, a vector of shape m * 1.")
        return None
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.shape[1] != 1\
            or not y.size or not np.issubdtype(y.dtype, np.number):
        print("x has to be an numpy.array, a vector of shape m * 1.")
        return None
    if not isinstance(theta, np.ndarray) or theta.shape != (2, 1)\
            or not theta.size or not np.issubdtype(theta.dtype, np.number):
        print("theta has to be an numpy.array, a vector of shape 2 * 1.")
        return None
    X = np.concatenate((np.ones((x.shape[0], 1)), x), axis=1)
    predictions = X @ theta
    error = y - predictions
    cost = float(error.T.dot(error)[0, 0] / y.shape[0])
    plt.scatter(x, y)
    plt.plot(x, predictions, color='red')
    plt.vlines(x, y, predictions, colors='red', linestyles='dashed')
    plt.title(f'Cost: {cost:.7}')
    plt.show()
