import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z=z-np.max(z)
        softmax_z=np.exp(z) / np.sum(np.exp(z)) 
        return np.round(softmax_z, 4)

