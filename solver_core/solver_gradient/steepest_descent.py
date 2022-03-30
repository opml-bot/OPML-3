import numpy as np
import pandas as pd
import plotly.graph_objects as go

from sympy import Symbol
from sympy import lambdify
from typing import Optional, Callable
from plotly.subplots import make_subplots


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
                 save_iters_df: Optional[bool] = False,
                 draw_flag: Optional[bool] = False):
        self.function = function
        self.gradient = gradient
        self.started_point = started_point
        self.max_iteration = max_iteration
        self.acc = acc
        self.print_midterm = print_midterm
        self.save_iters_df = save_iters_df
        self.draw_flag = draw_flag

    def solve(self):
        ans = ''
        if self.draw_flag:
            if self.started_point.shape[0] != 2:
                self.draw_flag = False # Может стоит бросать Error?
            else:
                draw_data = pd.DataFrame(columns=['x', 'y', 'z', 'iter', 'size'])
        if self.save_iters_df:
            iters_df = pd.DataFrame(columns=['f(x)', 'x'])
        alpha = Symbol('alpha')
        new_x = self.started_point
        for i in range(self.max_iteration):
            x_prev = new_x
            # вывод промежуточных
            if self.print_midterm:
                f_x = self.function(new_x)
                ans += f'iter{i:>5} f(x): {f_x:>.4f}\n'
            # сохранение в датафрейм
            if self.save_iters_df:
                if not self.print_midterm:
                    f_x = self.function(new_x)
                iters_df = iters_df.append({'f(x)': f_x, 'x': new_x}, ignore_index=True)
            # рисовалка
            if self.draw_flag:
                if not self.print_midterm and not self.save_iters_df:
                    f_x = self.function(new_x)
                draw_data = draw_data.append({'x': float(new_x[0]),
                                              'y': float(new_x[1]),
                                              'z': float(f_x),
                                              'iter': int(i),
                                              'size': 3}, ignore_index=True)

            gradient_xprev = self.gradient(self.function, x_prev)
            if self.stop_criterion(gradient_xprev):
                code = 0
                break
            steepest_step = x_prev - alpha*gradient_xprev
            alpha_eq = self.function(steepest_step)
            alpha_numeric = self.one_dim_opt(alpha_eq)
            new_x = x_prev - alpha_numeric*gradient_xprev

        else:
            code = 1
        ans += f'x: {new_x}\ny: {self.function(new_x)}\ncode: {code}\niters: {i+1}'
        if self.draw_flag:
            fig = self.draw(data=draw_data)
            return ans, fig
        return ans

    def one_dim_opt(self, eq):
        """
        Решает задачу одномерной оптимизации методом Брента.

        Parameters
        ----------
        eq: sympy выражение
            Задача, которую надо решить (с символом alpha)

        Returns
        -------
        x: float
            Точка минимума.
        """

        f = lambdify(['alpha'], eq)
        task = Brandt(f, [0, 1]) # спорный момент: границы поиска минимума. Стоит уточнить.
        x = task.solve()
        return x

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
        gradient_len = np.sqrt(sum([i**2 for i in grad]))
        if gradient_len < self.acc:
            return True
        else:
            return False

    def draw(self, data, ppa=50):
        if data.shape[0] > 50:
            step = data.shape[0]//50
            data = data.iloc[:, ::step]

        razm_x1 = data['x'].max() - data['x'].min()
        interval_x1 = [data['x'].min() - 0.2*razm_x1, data['x'].max() + 0.2*razm_x1]
        razm_x2 = data['x'].max() - data['x'].min()
        interval_x2 = [data['y'].min() - 0.2*razm_x2, data['y'].max() + 0.2*razm_x2]

        df = self.prepare_surface(interval_x1=interval_x1, interval_x2=interval_x2, cnt_points=ppa)
        min_value = min(filter(np.isfinite, df.values.flatten()))
        max_value = max(filter(np.isfinite, df.values.flatten()))
        fig = make_subplots(rows=1, cols=1, specs=[[{'is_3d': True}]])
        fig.add_trace(go.Surface(x=df.index,
                                 y=df.columns,
                                 z=df.values.T,
                                 opacity=0.5,
                                 showscale=False,
                                 colorscale='plasma',
                                 name='f(x, y)'),
                      row=1, col=1)
        fig.add_trace(go.Scatter3d(x=data.x,
                                   y=data.y,
                                   z=data.z,
                                   opacity=0.7,
                                   mode='lines',
                                   line={'width': 10}),
                      row=1, col=1)
        df_for_cone = self.prepare_arrows(df=data)

        fig.add_trace(go.Cone(x=df_for_cone.x,
                              y=df_for_cone.y,
                              z=df_for_cone.z,
                              u=df_for_cone.u,
                              v=df_for_cone.v,
                              w=df_for_cone.w,
                              showscale=False, sizeref=0.2))
        fig.update_scenes(xaxis={'range': interval_x1},
                          yaxis={'range': interval_x2}, row=1, col=1)
        # fig.add_trace(go.Contour(x=df.index,
        #                          y=df.columns,
        #                          z=df.values.T,
        #                          opacity=0.75,
        #                          contours={
        #                              'start': min_value,
        #                              'end': max_value,
        #                              'size': (max_value - min_value) // 15,
        #                          },
        #                          colorscale='ice',
        #                          name='f(x, y)'),
        #               row=1, col=1)
        return fig

    def prepare_surface(self, interval_x1, interval_x2, cnt_points):
        """

        Parameters
        ----------
        interval_x1
        interval_x2
        cnt_points

        Returns
        -------

        """
        x_axis = np.linspace(interval_x1[0], interval_x1[1], cnt_points)
        y_axis = np.linspace(interval_x2[0], interval_x2[1], cnt_points)
        points = pd.DataFrame(index=x_axis, columns=y_axis)
        x_axis = list(x_axis)
        y_axis = list(y_axis)

        for x_i in x_axis:
            for y_i in y_axis:
                f = self.function([x_i, y_i])
                if np.isfinite(f):
                    points.loc[x_i, y_i] = f
                else:
                    points.loc[x_i, y_i] = np.nan

        return points

    def prepare_arrows(self, df):
        """

        Parameters
        ----------
        df

        Returns
        -------

        """

        xdata = df.x.values.astype(np.float32)
        ydata = df.y.values.astype(np.float32)
        zdata = df.z.values.astype(np.float32)
        df_for_cone = pd.DataFrame({'x': xdata, 'y': ydata, 'z': zdata})
        veclen = list(np.sqrt(df_for_cone['x'] ** 2 + df_for_cone['y'] ** 2 + df_for_cone['z'] ** 2))
        df_for_cone['u'] = list((df_for_cone['x'] - df_for_cone['x'].shift()))
        df_for_cone['v'] = list((df_for_cone['y'] - df_for_cone['y'].shift()))
        df_for_cone['w'] = list((df_for_cone['z'] - df_for_cone['z'].shift()))
        print(df_for_cone)
        return df_for_cone


if __name__ == '__main__':
    func = lambda x: (x[0] - 50)**2 + x[1]**2
    gradient = lambda z, x: np.array([2*(x[0]-50), 2*x[1]])
    point = np.array([5, 5])

    task = SteepestGradient(function=func, gradient=gradient, started_point=point, print_midterm=1, max_iteration=5,
                            draw_flag=True)
    answer = task.solve()
    print(answer[0])
    answer[1].show()
