import numpy as np


def mse_(y, y_hat):
    """Description:
    Calculate the MSE between the predicted output and the real output.
Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
Returns:
    mse: has to be a float.
    None if there is a matching shape problem.
Raises:
    This function should not raise any Exception."""
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.shape[1] != 1\
            or not y.size or not np.issubdtype(y.dtype, np.number):
        print("y has to be an numpy.array, a vector of shape m * 1.")
        return None
    if not isinstance(y_hat, np.ndarray) or y_hat.ndim != 2 or\
            y_hat.shape[1] != 1 or not y_hat.size or\
            not np.issubdtype(y_hat.dtype, np.number):
        print("y_hat has to be an numpy.array, a vector of shape m * 1.")
        return None
    error = y - y_hat
    return float(error.T.dot(error)[0, 0] / y.shape[0])


def rmse_(y, y_hat):
    """Description:
    Calculate the RMSE between the predicted output and the real output.
Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
Returns:
    rmse: has to be a float.
    None if there is a matching shape problem.
Raises:
    This function should not raise any Exception."""
    mse = mse_(y, y_hat)
    if mse is None:
        return None
    return float(mse ** 0.5)


def mae_(y, y_hat):
    """Description:
    Calculate the MAE between the predicted output and the real output.
Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
Returns:
    mae: has to be a float.
    None if there is a matching shape problem.
Raises:
    This function should not raise any Exception."""
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.shape[1] != 1\
            or not y.size or not np.issubdtype(y.dtype, np.number):
        print("y has to be an numpy.array, a vector of shape m * 1.")
        return None
    if not isinstance(y_hat, np.ndarray) or y_hat.ndim != 2 or\
            y_hat.shape[1] != 1 or not y_hat.size or\
            not np.issubdtype(y_hat.dtype, np.number):
        print("y_hat has to be an numpy.array, a vector of shape m * 1.")
        return None
    absolute_error = abs(y - y_hat)
    return float(absolute_error.sum() / y.shape[0])


def r2score_(y, y_hat):
    """Description:
    Calculate the R2score between the predicted output and the output.
Args:
    y: has to be a numpy.array, a vector of shape m * 1.
    y_hat: has to be a numpy.array, a vector of shape m * 1.
Returns:
    r2score: has to be a float.
    None if there is a matching shape problem.
Raises:
    This function should not raise any Exception."""
    if not isinstance(y, np.ndarray) or y.ndim != 2 or y.shape[1] != 1\
            or not y.size or not np.issubdtype(y.dtype, np.number):
        print("y has to be an numpy.array, a vector of shape m * 1.")
        return None
    if not isinstance(y_hat, np.ndarray) or y_hat.ndim != 2 or\
            y_hat.shape[1] != 1 or not y_hat.size or\
            not np.issubdtype(y_hat.dtype, np.number):
        print("y_hat has to be an numpy.array, a vector of shape m * 1.")
        return None
    error = y - y_hat
    numerator = float(error.T.dot(error)[0, 0])
    denominator = ((y - y.mean()) ** 2).sum()
    return 1 - numerator / denominator
