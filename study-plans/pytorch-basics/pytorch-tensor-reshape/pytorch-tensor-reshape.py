import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x, dtype = torch.float32)

    if op == 'flatten':
        return x.flatten()
    if op == 'squeeze':
        return x.squeeze().tolist()
    if op == 'transpose':
        return x.T.tolist()
    pass
