import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v_arr = np.array(v)
    
    magnitude = np.linalg.norm(v_arr, axis=-1, keepdims=True)
    
    magnitude = np.where(magnitude == 0, 1, magnitude)
    
    return v_arr / magnitude
    pass