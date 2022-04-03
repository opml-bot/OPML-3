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
    text = HTMLMath(
        value=INPUT_FUNCTION
    )
    text = Text(value=' ',
                placeholder='Впиши функцию!',
                description='Функция:',
                layout=Layout(width='80%', height='80px'),
                disabled=False)

    def callback(wdgt):
        global params
        try:
            a = wdgt.value
            check_expression(a)
        except:
            pass
        params['function'] = wdgt.value
        text.layout.display = 'none'
        message_func.layout.display = 'none'
        set_grad()

    text.on_submit(callback)
    display(message_func)
    display(text)