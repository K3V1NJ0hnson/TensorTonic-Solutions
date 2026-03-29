import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    scores= torch.matmul(Q,K.transpose(-2,-1)) / math.sqrt(K.size(-1))
    attn_weights = F.softmax(scores, dim = -1)
    return torch.matmul(attn_weights, V)
    pass