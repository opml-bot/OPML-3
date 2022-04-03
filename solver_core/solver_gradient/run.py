from IPython.display import display
from ipywidgets import Dropdown, Textarea, Layout, Button, Text, HTMLMath,IntSlider, FloatText

from gradient_descent_const import GradientDescentConst
from gradient_descent_frac import GradientDescentFrac
from steepest_descent import SteepestGradient
#from solver_core.solver_gradient.handlers.input_validation import *
from messages import *


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
        layout=Layout(width='80%', height='80px'),
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
    print('MISWORKING!!!')