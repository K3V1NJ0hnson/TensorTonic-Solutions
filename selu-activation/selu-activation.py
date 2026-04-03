import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    x = np.array(x)
    
    # np.where works like an 'if' statement for every element in the array
    val = np.where(x > 0, 
                   lam * x, 
                   lam * alpha * (np.exp(np.clip(x, -500, 500)) - 1))
    
    # Return as a list rounded to 4 places
    return [round(float(v), 4) for v in val]
    pass

