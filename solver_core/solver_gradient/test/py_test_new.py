import pytest
import numpy as np
from solver_core.solver_gradient.gradient_descent_const import GradientDescentConst
from solver_core.solver_gradient.gradient_descent_frac import GradientDescentFrac
from solver_core.solver_gradient.handlers.preprocessing import *
from solver_core.solver_gradient.handlers.input_validation import *
import sympy as sp
from solver_core.solver_gradient.steepest_descent import SteepestGradient
from solver_core.solver_gradient.test.funcs import funcs
from solver_core.solver_gradient.test.funcs_str import funcs_str

EPS: float = 0.0001


# @pytest.mark.skipif(sys.version_info < (3,3),reason="requires python3.3")
def test_gradient_const():
    for names in funcs.keys():
        print(names)
        xs = list(sp.symbols('x1 x2'))
        point = prepare_point(funcs[names][2])
        flag_OK = sum(abs(np.array(list(
            map(float, GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
                       4:-1].split()))) - np.array(funcs[names][1]))) < EPS
        assert flag_OK

def test_gradient_frac():
    for names in funcs.keys():
        print(names)
        xs = list(sp.symbols('x1 x2'))
        point = prepare_point(funcs[names][2])
        flag_OK = sum(abs(np.array(list(
            map(float, GradientDescentFrac(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
                       4:-1].split()))) - np.array(funcs[names][1]))) < EPS
        assert flag_OK

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


def test_gradient_steepest():
    import math

    for names in funcs_str.keys():
        print(names)
        a = prepare_all(*funcs_str[names])
        print(a)
        flag_OK = sum(abs(np.array(list(
            map(float, SteepestGradient(a[0][0], a[0][1], a[0][2]).solve().split('\n')[0][
                       4:-1].split()))) - np.array(a[1]))) < EPS
        assert flag_OK
# for names in funcs.keys():
#     xs = list(sp.symbols('x1 x2'))
#     point = prepare_point(funcs[names][2])
#     print(np.array(
#         list(map(float, GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
#                         4:-1].split()))))
#     break
