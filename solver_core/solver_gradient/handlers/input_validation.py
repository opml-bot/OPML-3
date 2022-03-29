import re

from typing import Optional
from sympy.parsing.sympy_parser import parse_expr
from sympy import sympify, exp

ALLOWED_OPERATIONS = ['log', 'ln', 'factorial', 'sin', 'cos', 'tan', 'cot', 'pi', 'exp', 'sqrt', 'root', 'abs']


def check_expression(expression: str) -> tuple:
    """
    Функция для проверки выражения на корректность. Принимает на вход строку с функцией
    в аналитическом виде, возвращает строку. Функция обязательно должна быть
    только от аргументов вида x1, x2, ..., xn.

    Parameters:
    ------------
    expression: str
        Строка содержащая функцию для проверки.

    Returns:
    -------
    str: str
        Функция в виде строки.

    variables: list
        Список переменных функции.
    """

    expression = expression.strip()
    if expression.find('—') != -1:
        expression = expression.replace('—', '-')

    if expression.find('–') != -1:
        expression = expression.replace('–', '-')

    checker = compile(expression, '<string>', 'eval')  # Может выдать SyntaxError, если выражение некорректно
    var_checker = re.compile(r'^x{1}[0-9]+$')

    for name in checker.co_names:
        if name not in ALLOWED_OPERATIONS:
            if not (var_checker.match(name) and name != 'x0'):
                raise NameError(f"The use of '{name}' is not allowed")

    function = sympify(expression, {'e': exp(1)}, convert_xor=True)
    variables = [str(i) for i in list(function.free_symbols)]
    return str(function), variables


def check_gradients(grad_str: str, var: list, splitter: Optional[str] = ';') -> str:
    """
    Проверяет корректность и читаемость градиентов, а также сверяет количество градиентов с количеством переменных.
    Если в качестве s передали 'False' или пустую строку, то никаких обработок в дальнейшем не будет, а градиент
    будет чситаться численно.

    Parameters
    ----------
    grad_str: str
        Строка с градиентами в аналитическом виде.

    var: list
        Список переменных.

    splitter: Optional[str] = ';'
        Строка-разделитель, которым разделены градиенты.

    Returns
    -------
    grads: str
        Строка с градиентами в аналитическом виде, разделенные ';'.
    """

    if grad_str == '' or grad_str == 'False':
        return grad_str
    nvars = int(max(var, key=lambda x: int(x[1:]))[1:])

    g = grad_str.split(splitter)
    if len(g) < nvars:
        raise ValueError(f'Введено меньше градиентов чем переменных: {len(g)} < {nvars}')
    else:
        ans = []
        for i in range(len(g)):
            ans.append(check_expression(g[i])[0])
    grads = ";".join(ans)
    return grads


def check_float(value: str) -> float:
    """
    Проверяет введеное значение на корректность и на наличие инъекций, а затем
    конвертирует в float, если это возможно. Поддерживает операции с pi и e.
    Parameters:
    ------------
    values: str
        строка в которой содержится выражение
    Returns:
    -------
    float
        значение переведенное из строки в float
    """
    if value.find('^') != -1:
        value = value.replace('^', '**')
    checker = compile(value, '<string>', 'eval')  # Может выдать SyntaxError, если выражение некорректно
    for name in checker.co_names:
        if name not in ['pi', 'e', 'exp']:
            raise ValueError(f'Нельзя использовать имя {name}')
    value = float(parse_expr(value, {'e': exp(1)}))
    return value


def check_int(value: str) -> int:
    """
    Проверяет введеное значение на корректность и на наличие инъекций, а затем
    конвертирует в int, если это возможно.
    Parameters:
    ------------
    values: str
        строка в которой содержится выражение
    Returns:
    -------
    int
        значение переведенное из строки в int
    """
    if value.find('^') != -1:
        value = value.replace('^', '**')
    value = int(parse_expr(value))
    return value


if __name__ == '__main__':
    func = '(x1-2)**2 + (x3 - 4)**2 + x4'
    grad = '2*(x1-2);0; 2*(x3 - 4); 1'

    s = check_expression(func)
    print(s[0], s[1])
    print(check_gradients(grad_str=grad, var=s[1]))
    print(check_float('10^-5'))