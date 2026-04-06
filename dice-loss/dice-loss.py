import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.array(p)
    y = np.array(y)
    numerator = 2 * np.sum(p * y) + eps
    denom = np.sum(p) + np.sum(y) + eps
    dice = numerator / denom

    loss = 1 - dice
    return loss
    pass