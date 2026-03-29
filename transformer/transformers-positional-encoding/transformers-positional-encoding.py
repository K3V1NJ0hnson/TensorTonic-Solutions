import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    pe = np.zeros((seq_length, d_model))
    pos = np.arange(seq_length).reshape(-1, 1)

    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))

    # Even columns (0, 2, 4...)
    pe[:, 0::2] = np.sin(pos * div_term)

    # Odd columns (1, 3, 5...)
    pe[:, 1::2] = np.cos(pos * div_term)

    return pe
    pass