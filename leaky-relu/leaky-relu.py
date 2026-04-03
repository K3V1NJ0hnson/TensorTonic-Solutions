import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x= np.array(x)

    val = np.where(x < 0,
                  alpha * x,
                  x)
    return np.array([round(float(v),4) for v in val])
    pass