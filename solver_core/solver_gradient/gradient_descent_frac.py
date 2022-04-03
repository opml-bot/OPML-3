from typing import Optional, Callable
from math import sqrt, exp
import numpy as np
import math



class GradientDescentFrac:

    def __init__(self,
                 function: Callable,
                 gradient: Callable,
                 started_point: np.ndarray,
                 alpha: float = 1e-1,
                 delta: float = 1e-1,
                 max_iteration: Optional[int] = 500,
                 acc: Optional[float] = 10 ** -5,
                 print_midterm: Optional[bool] = False,
                 save_iters_df: Optional[bool] = False):

        self.function = function
        self.gradient = gradient
        self.started_point = started_point
        self.alpha = alpha
        self.delta = delta
        self.max_iteration = max_iteration
        self.acc = acc
        self.print_midterm = print_midterm
        self.save_iters_df = save_iters_df

    def solve(self):
        alpha = self.alpha
        new_x = self.started_point
        grad_k = self.gradient(self.function, new_x)
        func_k = self.function(new_x)
        for i in range(self.max_iteration):
            t = new_x - alpha * grad_k
            func_t = self.function(t)

            while not func_t - func_k <= - alpha * 0.1 * sum(grad_k ** 2):
                alpha = alpha * self.delta
                t = new_x - alpha * grad_k
                func_t = self.function(t)

            new_x = t
            func_k = func_t
            grad_k = self.gradient(self.function, new_x)
            x_prev = new_x
            gradient_xprev = self.gradient(self.function, x_prev)

            if self.stop_criterion(gradient_xprev):
                code = 0
                break

        else:
            code = 1
        ans = f'x: {new_x}\ny: {self.function(new_x)}\ncode: {code}\niters: {i + 1}'
        return ans

    def stop_criterion(self, grad):
        """
        Метод проверяет критерий остановки. В качетсве критерия остановки используется длина градиента.
        Parameters
        ----------
        grad: np.ndarray
             Градиент в точке
        Returns
        -------
        bool
            True, если достигнута заданная точность, иначе - False
        """
        gradient_len = np.sqrt(sum([i ** 2 for i in grad]))
        if gradient_len < self.acc:
            return True
        else:
            return False


if __name__ == '__main__':
    func = lambda x: x[0] ** 2 + x[1] ** 2
    gradient = lambda z, x: np.array([2 * x[0], 2 * x[1]])
    point = [5, 5]

    task = GradientDescentFrac(function=func, gradient=gradient, started_point=point)
    answer = task.solve()
    print(answer)
