import pandas as pd
from scipy.optimize import minimize

df = pd.DataFrame(
    columns=['Название', 'Вводные данные', 'Алгоритм1', \
             'Алгоритм2', 'Алгоритм3', 'Алгоритм4', 'scipy', 'Верный ответ'])
for k, names in enumerate(funcs.keys()):
    df.loc[k] = [f'{names}', f'x = ({funcs[names][2]})',\
             f"{GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve()}", f'', f'', f'',\
             f'{minimize(funcs[names][0], funcs[names][2])}', f'{funcs[names][1]}']
print(df)