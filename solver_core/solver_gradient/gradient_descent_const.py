from typing import Optional, Callable
from math import sqrt, exp
import numpy as np
import pandas as pd
import math


class GradientDescentConst:

    def __init__(self,
                 function: Callable,
                 gradient: Callable,
                 started_point: np.ndarray,
                 alpha: float = 1e-1,
                 max_iteration: Optional[int] = 500,
                 acc: Optional[float] = 10 ** -5,
                 print_midterm: Optional[bool] = False,
                 save_iters_df: Optional[bool] = False):

        self.function = function
        self.gradient = gradient
        self.started_point = started_point
        self.alpha = alpha
        self.max_iteration = max_iteration
        self.acc = acc
        self.print_midterm = print_midterm
        self.save_iters_df = save_iters_df
        self.history = pd.DataFrame(columns=['x', 'f', 'iteration'])

    def solve(self):
        alpha = self.alpha
        new_x = self.started_point

        # Будем сохранять историю для каждой итерации. Чтобы нарисовать спуск нужно точки x и значение f
        # Для этого я создал пустой датафрейм в конструкторе и буду его заполнять
        if self.save_iters_df:
            self.history.loc[0] = [np.array(new_x), self.function(new_x), 0]

        for i in range(self.max_iteration):
            x_prev = new_x
            gradient_xprev = self.gradient(self.function, x_prev)
            if self.stop_criterion(gradient_xprev):
                code = 0
                break

            new_x = x_prev - alpha * gradient_xprev

            if self.save_iters_df:
                self.history.loc[i + 1] = [new_x, self.function(new_x), i + 1]

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

    task = GradientDescentConst(function=func, gradient=gradient, started_point=point)
    answer = task.solve()
    print(answer)
