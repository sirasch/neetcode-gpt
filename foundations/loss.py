import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
    
        n = len(y_true)
        eps = np.finfo(float).eps
        return np.round(-np.sum(
        y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps)
        ) / n, 4)


    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        n = len(y_true)
        eps = np.finfo(float).eps
        return np.round(-np.sum(
        y_true * np.log(y_pred + eps)
        ) / n, 4)
