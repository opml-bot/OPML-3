import numpy as np

from sympy import Symbol
from typing import Callable, Optional

class SteepestGradient:

    def __init__(self,
                 function: Callable,
                 gradient: Callable,
                 started_point: np.ndarray,
                 max_iteration: Optional[int] = 500,
                 acc: Optional[float] = 10**-5,
                 print_midterm: Optional[bool] = False,
                 save_iters_df: Optional[bool] = False):
        self.function = function
        self.gradient = gradient
        self.started_point = started_point
        self.max_iteration = max_iteration
        self.acc = acc
        self.print_midterm = print_midterm
        self.save_iters_df = save_iters_df

    def solve(self):
        pass
