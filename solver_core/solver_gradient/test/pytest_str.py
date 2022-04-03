from solver_core.solver_gradient.handlers.preprocessing import *
from solver_core.solver_gradient.handlers.input_validation import *
from solver_core.solver_gradient.gradient_descent_const import GradientDescentConst
from solver_core.solver_gradient.gradient_descent_frac import GradientDescentFrac
from solver_core.solver_gradient.steepest_descent import SteepestGradient

from test_str import funcs

def prepare_all(func, min_val, point):
    func = func(0,0)
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


for i in funcs:
    a = prepare_all(*funcs[i])
    task = GradientDescentConst(function=a[0][0], gradient=a[0][1], started_point=a[0][2])
    print(task.solve())
