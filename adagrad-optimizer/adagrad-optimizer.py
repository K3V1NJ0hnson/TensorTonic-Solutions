import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)
    grad_squared = g**2 + G

    denom = np.sqrt(grad_squared + eps)
    adaptation = lr / denom
    w_new = w - (adaptation * g)
    return (w_new, grad_squared)
    pass