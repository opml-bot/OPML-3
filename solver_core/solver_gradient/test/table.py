import pandas as pd
from scipy.optimize import minimize
from funcs import funcs
import sympy as sp
from solver_core.solver_gradient.gradient_descent_const import GradientDescentConst
from solver_core.solver_gradient.handlers.preprocessing import prepare_gradient
from solver_core.solver_gradient.handlers.preprocessing import prepare_point

df = pd.DataFrame(
    columns=['Название', 'Вводные данные', 'Алгоритм1', \
             'Алгоритм2', 'Алгоритм3', 'Алгоритм4', 'scipy', 'Верный ответ'])
for k, names in enumerate(funcs.keys()):
    xs = list(sp.symbols('x1 x2'))
    point = prepare_point(funcs[names][2])
    df.loc[k] = [f'{names}', f'x = ({funcs[names][2]})',\
             GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0], f'', f'', f'',\
             f'x = {minimize(funcs[names][0], point).x}', f'{funcs[names][1]}']
# print(df)
print(df.to_latex(index=False))