import pytest
from funcs import funcs
from scipy.optimize import minimize

EPS = 0.0001

def test_graient_const():
    for names in funcs.keys():
        assert minimize(funcs[names][0],funcs[names][1])-