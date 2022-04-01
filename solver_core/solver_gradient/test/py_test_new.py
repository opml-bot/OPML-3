import pytest
from funcs import funcs
import numpy as np
from solver_core.solver_gradient.gradient_descent_const import GradientDescentConst
from solver_core.solver_gradient.gradient_descent_frac import GradientDescentFrac
from solver_core.solver_gradient.handlers.preprocessing import prepare_gradient
from solver_core.solver_gradient.handlers.preprocessing import prepare_point
import sympy as sp

from solver_core.solver_gradient.steepest_descent import SteepestGradient

EPS = 0.0001


# @pytest.mark.skipif(sys.version_info < (3,3),reason="requires python3.3")
def test_graient_const():
    for names in funcs.keys():
        print(names)
        xs = list(sp.symbols('x1 x2'))
        point = prepare_point(funcs[names][2])
        flag_OK = sum(abs(np.array(list(
            map(float, GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
                       4:-1].split()))) - np.array(funcs[names][1]))) < EPS
        assert flag_OK
def test_graient_frac():
    for names in funcs.keys():
        print(names)
        xs = list(sp.symbols('x1 x2'))
        point = prepare_point(funcs[names][2])
        flag_OK = sum(abs(np.array(list(
            map(float, GradientDescentFrac(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
                       4:-1].split()))) - np.array(funcs[names][1]))) < EPS
        assert flag_OK
def test_graient_steepest():
    for names in funcs.keys():
        print(names)
        xs = list(sp.symbols('x1 x2'))
        point = prepare_point(funcs[names][2])
        flag_OK = sum(abs(np.array(list(
            map(float, SteepestGradient(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
                       4:-1].split()))) - np.array(funcs[names][1]))) < EPS
        assert flag_OK
# for names in funcs.keys():
#     xs = list(sp.symbols('x1 x2'))
#     point = prepare_point(funcs[names][2])
#     print(np.array(
#         list(map(float, GradientDescentConst(funcs[names][0], prepare_gradient('', xs), point).solve().split('\n')[0][
#                         4:-1].split()))))
#     break
