def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """

    L = np.sqrt(6/fan_in)
    return np.array(W) * 2 * L - L