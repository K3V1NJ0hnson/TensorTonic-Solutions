import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x_arr = np.array(x)

    sigmoid = 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    return x * sigmoid
    
    pass