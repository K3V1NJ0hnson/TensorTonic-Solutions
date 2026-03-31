import numpy as np

def relu(x):
    return np.maximum(0, x)

class ConvBlock:
    """
    Convolutional Block with projection shortcut.
    Used when input/output dimensions differ.
    """
    
    def __init__(self, in_channels: int, out_channels: int):
        self.in_channels = in_channels
        self.out_channels = out_channels
        
        # Main path weights
        self.W1 = np.random.randn(in_channels, out_channels) * 0.01
        self.W2 = np.random.randn(out_channels, out_channels) * 0.01
        
        # Shortcut projection (1x1 conv equivalent)
        self.Ws = np.random.randn(in_channels, out_channels) * 0.01
    
    def forward(self, x: np.ndarray) -> np.ndarray:
        """
        Forward pass with projection shortcut.
        """
        h = relu(x @ self.W1)
        f_x = h @ self.W2
        
        # 2. The Projection Shortcut (Ws @ x)
        # This transforms the original 'x' to match the output dimension
        shortcut = x @ self.Ws
        
        # 3. Combine and Return
        # Standard ResNet applies one last ReLU after the addition
        return relu(f_x + shortcut)
        pass
