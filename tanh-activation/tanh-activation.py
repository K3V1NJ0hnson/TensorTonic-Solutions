import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    tanh_fx = (np.exp(np.clip(x, -500,500)) - np.exp(-np.clip(x, -500,500))) / (np.exp(np.clip(x, -500,500)) + np.exp(-np.clip(x, -500,500)))
    
    return tanh_fx
    pass