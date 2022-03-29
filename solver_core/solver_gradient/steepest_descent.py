from sympy import Symbol

from typing import Optional, Callable
import numpy as np



class Brandt:
    """
        Класс для решения задачи поиска минимума одномерной функции на отрезке комбинированным методом Брента.
        Parameters
        ----------
        func : Callble
            Функция, у которой надо искать минимум.
        interval_x : tuple
            Кортеж с двумя значениями типа float, которые задают ограничения для отрезка.
        acc: Optional[float] = 10**-5
            Точность оптимизации. Выражается как разница иксов на n и n-1 итерации. По умолчанию 10**-5
        max_iteration: Optional[int] = 500
            Максимально допустимое количество итераций. По умолчанию 500.
        print_interim: Optional[bool] = False
            Флаг, нужно ли сохранять информацию об итерациях. Информация записывается в строку с ответом.
        save_iters_df: Optional[bool] = False
            Флаг, нужно ли сохранять информацию об итерациях в pandas.DataFrame, который будет возвращаться дополнительно
            в методе solve.
        """

    def __init__(self, func: Callable,
                 interval_x: tuple,
                 acc: Optional[float] = 10**-5,
                 max_iteration: Optional[int] = 500):
        self.func = func
        self.interval_x = interval_x
        self.acc = acc
        self.max_iteration = max_iteration

    def solve(self):
        """
        Метод решает созданную задачу.
        Returns
        ---------
        ans: float
            Ответ в виде числа x.
        """
        # инициализация начальных значений
        t = 10**-8

        a, b = self.interval_x
        C = (3 - 5**0.5)/2
        x0 = a + C*(b - a)
        x1 = x2 = x0
        d = e = 0
        f0 = f1 = f2 = self.func(x0)

        # начало алгоритма
        for i in range(self.max_iteration):

            m = 0.5 * (a + b)
            tol = self.acc*abs(x0) + t
            t2 = 2*tol


            # критерий остановки
            if abs(x0 - m) <= t2 - 0.5*(b - a):
                break

            r = 0
            q = r
            p = q

            if tol < abs(e):
                r = (x0 - x1)*(f0 - f2)
                q = (x0 - x2)*(f0 - f1)
                p = (x0 - x2)*q - (x0 - x1)*r
                q = 2*(q - r)
                if 0 < q:
                    p = -p
                q = abs(q)
                r = e
                e = d

            if abs(p) < abs(0.5*q*r) and q*(a - x0) < p and p < q * (b - x0):
                # Шаг методом парабол
                d = p/q
                u = x0 + d

                # Значения функции не должны быть очень близки к границам интервала
                if (u - a) < t2 or (b - u) < t2:
                    if x0 < m:
                        d = tol
                    else:
                        d = -tol
            else:
                # Шаг методом золотого сечения
                if x0 < m:
                    e = b - x0
                else:
                    e = a - x0
                d = C*e

                # Новая функция не должна быть слишком близка к x0
                if tol <= abs(d):
                    u = x0 + d
                elif 0 < d:
                    u = x0 + tol
                else:
                    u = x0 - tol

            fu = self.func(u)

            if fu <= f0:

                if u < x0:
                    if b != x0:
                        b = x0
                else:
                    if a != x0:
                        a = x0

                x2 = x1
                f2 = f1
                x1 = x0
                f1 = f0
                x0 = u
                f0 = fu

            else:
                if u < x0:
                    if a != u:
                        a = u
                else:
                    if b != u:
                        b = u

                if fu <= f1 or x1 == x0:
                    x2 = x1
                    f2 = f1
                    x1 = u
                    f1 = fu
                elif fu <= f2 or x2 == x0 or x2 == x1:
                    x2 = u
                    f2 = fu
        return x0


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
        alpha = Symbol('alpha')
        x_prev = self.started_point
        for i in range(self.max_iteration):
            steepest_step = x_prev - alpha*self.gradient(x_prev)
            alpha_eq = self.function(steepest_step)
            alpha_numeric = alpha_eq


if __name__ == '__main__':
    func = lambda x: x[0]**2 + x[1]**2
    gradient = lambda x: np.array([2*x[0], 2*x[1]])
    point = [5, 5]

    task = SteepestGradient(function=func, gradient=gradient, started_point=point)
    task.solve()
