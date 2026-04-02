import numpy as np

def compute_gradient_with_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITH skip connections.
    Gradient at layer l = sum of paths through network
    """
    result = x.copy().reshape(-1, 1)          # ensure column vector (n, 1)
    
    for G in reversed(gradients_F):
        G_mat = np.array(G)      # shape (n, n)
        n = G_mat.shape[0]
        I = np.eye(n)
        result = (G_mat + I) @ result         # matrix @ column
    
    return result.flatten()

def compute_gradient_without_skip(gradients_F: list, x: np.ndarray) -> np.ndarray:
    """
    Compute gradient flow through L layers WITHOUT skip connections.
    """
    result = x.copy().reshape(-1, 1)          # ensure column vector
    
    for G in reversed(gradients_F):
        G_mat = np.array(G)
        result = G_mat @ result
    
    return result.flatten()
    pass
