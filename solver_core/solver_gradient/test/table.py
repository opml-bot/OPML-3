import pandas as pd
from scipy.optimize import minimize
from funcs import funcs
import sympy as sp
from solver_core.solver_gradient.gradient_descent_const import GradientDescentConst
from solver_core.solver_gradient.gradient_descent_frac import GradientDescentFrac
from solver_core.solver_gradient.handlers.preprocessing import *
from solver_core.solver_gradient.handlers.input_validation import *
from solver_core.solver_gradient.newtonCG import NewtonCG
from solver_core.solver_gradient.steepest_descent import SteepestGradient
from solver_core.solver_gradient.test.funcs_str import funcs_str


def prepare_all(func, min_val, point):
    func = func(0, 0)
    s, vars = check_expression(func)
    grad = check_gradients('', vars)
    point = check_point(point)
    check_dimension(vars, point)

    vars = get_variables(s)
    func = prepare_func(s, vars)
    grads = prepare_gradient(grad, vars)
    point = prepare_point(point)
    min_val = prepare_point(check_point(min_val))
    return [func, grads, point], min_val


df = pd.DataFrame(
    columns=['Название', 'Вводные данные', 'Градиентный спуск с const шагом',
             'Градиентный спуск с дроблёным шагом', 'Наискорейший градиентный спуск',
             'Ньютона-сопряжённый градиентный спуск', 'scipy', 'Верный ответ'])
for k, names in enumerate(funcs.keys()):
    xs = list(sp.symbols('x1 x2'))
    point = prepare_point(funcs[names][2])
    a = prepare_all(*funcs_str[names])
    df.loc[k] = [f'{names}', f'x = ({funcs[names][2]})',
                 GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[1],
                 GradientDescentFrac(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[1],
                 SteepestGradient(a[0][0], a[0][1], a[0][2]).solve().split('\n')[0][
                 4:-1].split('\n')[0], NewtonCG(a[0][0], a[0][2]).solve().split('\n')[0][4:-1].split('\n')[0],
                 f'x = {minimize(funcs[names][0], point).x}', f'{funcs[names][1]}']
# print(df)
print(df.to_latex(index=False))
