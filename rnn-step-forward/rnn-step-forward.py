import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    rnn_cell = (np.matmul(x_t, Wx)) + (np.matmul(h_prev,Wh)) + b
    return np.tanh(rnn_cell)
    pass
