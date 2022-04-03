from IPython.display import display
from ipywidgets import Dropdown, Textarea, Layout, Button, Text, HTMLMath,IntSlider, FloatText

from .handlers.input_validation import *
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


def choose_method():
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
    text = Text(value=' ',
                placeholder='Впиши функцию!',
                description='Функция:',
                layout=Layout(width='80%', height='80px'),
                disabled=False)

    def callback(wdgt):
        global params
        global variables
        try:
            a = wdgt.value.strip()
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
                description='Функция:',
                layout=Layout(width='80%', height='80px'),
                disabled=False)
    def callback(wdgt):
        global params
        global variables
        try:
            a = wdgt.value.strip()
            a = check_gradients(a, variables)
        except SyntaxError as err:
            print(err)
        except NameError as err:
            print(err)
        else:
            params['gradient'] = a
            text.layout.display = 'none'
            message.layout.display = 'none'
            if len(variables) < 4:
                set_point_low()

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
        s = []
        for i in range(len(floats)):
            floats[i].layout.display = 'none'
            s.append(floats[i].value)
        s = ';'.join(s)
        try:
            a = check_point(s)
        except ValueError as err:
            print(err)
        try:
            check_dimension(variables, a)
        except:
            print('Все плохо, перезапусти ячейку(')
        confirm.layout.display = 'none'
        message.layout.display = 'none'
        params['point'] = a

    confirm.on_click(callback)
    display(message)
    display(confirm, *floats)


def set_point_high():
    message = HTMLMath(
        value=INPUT_POINT
    )
    text = Text(value=None, description=f'Координаты', disabled=False)

    def callback(wdgt):
        global params
        try:
            a = check_point(text.value.strip())
        except ValueError as err:
            print(err)
        try:
            check_dimension(variables, a)
        except:
            print('Все плохо, перезапусти ячейку(')
        message.layout.display = 'none'
        text.layout.display = 'none'
        params['point'] = a

    text.on_submit(callback)
    display(message)
    display(text)