class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
       x_c= init
       for n in range(iterations):
        x_new= x_c-2*learning_rate*x_c
        x_c=x_new
       return round(x_c, 5)
