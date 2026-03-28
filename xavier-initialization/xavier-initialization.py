def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    L = np.sqrt(6/(fan_in + fan_out))
    return np.array(W) * 2 * L - L