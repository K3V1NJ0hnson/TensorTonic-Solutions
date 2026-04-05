import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    w = np.array(w)
    m = np.array(m)
    v = np.array(v)
    grad = np.array(grad)
    
    first_moment = (beta1 * m) + ((1 - beta1) * grad)
    second_moment = (beta2 * v) + ((1 - beta2) * np.square(grad))
    nest_update = w - (lr * ((beta1 * first_moment) + (1 - beta1) * grad) / (np.sqrt(second_moment) + eps))
    return (nest_update, first_moment, second_moment)
    pass