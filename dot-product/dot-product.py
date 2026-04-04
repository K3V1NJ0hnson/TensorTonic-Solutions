import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x_arr = np.array(x)
    y_arr = np.array(y)
    return np.dot(x_arr, y_arr)
    pass