from IPython.display import display
from ipywidgets import Dropdown, Textarea, Layout, Button, Text, HTMLMath,IntSlider, FloatText, IntText, Checkbox

from .handlers.input_validation import *
from .handlers.preprocessing import *
from .gradient_descent_const import GradientDescentConst
from .gradient_descent_frac import GradientDescentFrac
from .steepest_descent import SteepestGradient
from .messages import *

# from gradient_descent_const import GradientDescentConst
# from gradient_descent_frac import GradientDescentFrac
# from steepest_descent import SteepestGradient
# from messages import *
# from solver_core.solver_gradient.handlers.input_validation import *


params = {}
variables = 0


def start():
    text = HTMLMath(
        value=HELLO_TEXT
    )
    dropdown1 = Dropdown(
        options=[('Градиент с константным шагом', GradientDescentConst),
                 ('Градиент с дроблением шага', GradientDescentFrac),
                 ('Наискорейший спуск', SteepestGradient)],
        value=None,  # Выбор по умолчанию
        layout=Layout(width='50%', height='20px'),
        description='Метод:')

    def on_button_clicked(b):
        global params
        params['Method'] = b['new']
        text.layout.display = 'none'
        dropdown1.layout.display = 'none'
        set_func()

    dropdown1.observe(on_button_clicked, names='value')
    display(text)
    display(dropdown1)


def set_func():
    message = HTMLMath(
        value=INPUT_FUNCTION
    )
    text = Text(value=None,
                placeholder='Впиши функцию!',
                description='Функция:',
                layout=Layout(width='80%', height='80px'),
                disabled=False)

    def callback(wdgt):
        global params
        global variables
        try:
            a = wdgt.value.strip()
            print(a)
            a = check_expression(a)
        except SyntaxError as err:
            print(err)
        except NameError as err:
            print(err)
        else:
            params['function'] = a[0]
            variables = a[1]
            text.layout.display = 'none'
            message.layout.display = 'none'
            set_grad()

    text.on_submit(callback)
    display(message)
    display(text)


def set_grad():
    message = HTMLMath(
        value=INPUT_GRADIENT
    )
    text = Text(value=' ',
                placeholder='Впиши функцию!',
                description='Градиент:',
                layout=Layout(width='80%', height='80px'),
                disabled=False)
    def callback(wdgt):
        global params
        global variables
        try:
            a = wdgt.value.strip()
            print(a)
            a = check_gradients(a, variables)
        except SyntaxError as err:
            print(err)
        except NameError as err:
            print(err)
        except ValueError as err:
            print(err)
        else:
            params['gradient'] = a
            text.layout.display = 'none'
            message.layout.display = 'none'
            if len(variables) < 4:
                set_point_low()
            else:
                set_point_high()

    text.on_submit(callback)
    display(message)
    display(text)


def set_point_low():
    message = HTMLMath(
        value=INPUT_POINT_LESS_TNEN_3
    )
    floats = []
    for i in range(len(variables)):
        floats.append(Text(value='0', description=f'x{i+1}:', disabled=False))
    confirm = Button(description='Подтвердить', disabled=False, button_style='info', tooltip='Click me', icon='check')

    def callback(wdgt):
        global params
        global variables
        s = []
        try:
            for i in range(len(floats)):
                floats[i].layout.display = 'none'
                s.append(floats[i].value)
            s = ';'.join(s)
        except:
            print('Попробуй еще раз')
        else:
            try:
                a = check_point(s)
            except ValueError as err:
                print(err)
            else:
                try:
                    check_dimension(variables, a)
                except:
                    print(f'Кажется размерности не совпадают, надо ввести {len(variables)} переменных.')
                else:
                    confirm.layout.display = 'none'
                    message.layout.display = 'none'
                    params['point'] = a
                    set_other()

    confirm.on_click(callback)
    display(message)
    display(confirm, *floats)


def set_point_high():
    message = HTMLMath(
        value=INPUT_POINT
    )
    text = Text(value=None, description=f' ', disabled=False)

    def callback(wdgt):
        global params
        global variables
        try:
            a = check_point(text.value.strip())
        except ValueError as err:
            print(err)
        else:
            try:
                check_dimension(variables, a)
            except:
                print(f'Кажется размерности не совпадают, надо ввести {len(variables)} переменных.')
            else:
                message.layout.display = 'none'
                text.layout.display = 'none'
                params['point'] = a
                set_other()

    text.on_submit(callback)
    display(message)
    display(text)


def set_other():
    message = HTMLMath(
        value=CONST_GRAD
    )
    extra = []
    if params['Method'] == GradientDescentConst:
        alpha = Text(value='1e-1', description=f'Alpha:', disabled=False)
        names = ['alpha']
        extra.append(alpha)
    if params['Method'] == GradientDescentFrac:
        alpha = Text(value='1e-1', description=f'Alpha:', disabled=False)
        delta = Text(value='1e-1', description=f'Delta:', disabled=False)
        names = ['alpha', 'delta']
        extra.append(alpha)
        extra.append(delta)
    if params['Method'] == SteepestGradient:
        names = []
    iteration = IntText(value=500, description='Макс. итераций', disabled=False)
    acc = Text(value='10**-5', description=f'Точность:', disabled=False)
    print_midterm = Checkbox(value=False, description='Выводить промежуточные резултаты?')
    save_iters_df = Checkbox(value=False, description='Сохранять результаты в dataframe?')
    confirm = Button(description='Подтвердить', disabled=False, button_style='info', tooltip='Click me', icon='check')
    def callback(wdgt):
        global params
        try:
            for i in range(len(extra)):
                params[names[i]] = check_float(extra[i].value)
        except ValueError as err:
            print(err)
        else:
            for i in range(len(extra)):
                extra[i].layout.display = 'none'
            try:
                iteration_ = iteration.value
            except TypeError:
                print('Не вышло, попробуй изменить число итераций')
            else:
                try:
                    acc_ = check_float(acc.value)
                except TypeError:
                    print('Не получилос, попробуй изменить точность')
                else:
                    iteration.layout.display = 'none'
                    acc.layout.display = 'none'
                    message.layout.display = 'none'
                    print_midterm.layout.display = 'none'
                    save_iters_df.layout.display = 'none'
                    confirm.layout.display = 'none'
                    params['acc'] = acc_
                    params['max_iter'] = iteration_
                    params['print_midterm'] = print_midterm.value
                    params['save_iters_df'] = save_iters_df.value
                    answer = calculate()
                    return answer

    c = confirm.on_click(callback)
    display(message)
    display(*extra, iteration, acc, print_midterm, save_iters_df, confirm)
    return c


def calculate():
    global params
    variables = get_variables(params['function'])
    func = prepare_func(params['function'], variables)
    grads = prepare_gradient(params['gradient'], variables)
    point = prepare_point(params['point'])
    max_iter = params['max_iter']
    accur = params['acc']
    printer = params['print_midterm']
    dataframe = params['save_iters_df']
    if params['Method'] == GradientDescentConst:
        alpha_ = params['alpha']
        task = GradientDescentConst(function=func, gradient=grads, started_point=point, alpha=alpha_,
                                    max_iteration=max_iter, acc=accur, print_midterm=printer, save_iters_df=dataframe)
        ans = task.solve()
    if params['Method'] == GradientDescentFrac:
        alpha_ = params['alpha']
        delta_ = params['delta']
        task = GradientDescentFrac(function=func, gradient=grads, started_point=point, alpha=alpha_, delta=delta_,
                                max_iteration=max_iter, acc=accur, print_midterm=printer, save_iters_df=dataframe)
        ans = task.solve()
    if params['Method'] == SteepestGradient:
        task = GradientDescentFrac(function=func, gradient=grads, started_point=point,
                                   max_iteration=max_iter, acc=accur, print_midterm=printer, save_iters_df=dataframe)
        ans = task.solve()
    return ans
