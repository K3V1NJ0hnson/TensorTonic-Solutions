import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    numerator = np.sum(np.square(y_true - y_pred))
    denom = np.sum(np.square(y_true - np.average(y_true)))
    if np.all(y_true == y_true[0]):
        return 1.0 if np.array_equal(y_true, y_pred) else 0.0
    
    return 1 - (numerator / denom)
    pass