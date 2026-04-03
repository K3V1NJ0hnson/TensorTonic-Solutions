import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x_arr = np.array(x)

    val = np.where(x_arr > 0,
                   x_arr,
                   alpha * (np.exp(np.clip(x,-500,500)) - 1))

    return [round(float(v), 4)for v in val]