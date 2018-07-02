# -*- coding: utf-8 -*-
from functools import partial
from inspect import signature

def mul(x, y):
    return x * y

def _partial(func, *args, **kwargs):
    _sig =  signature(func)
    def _wrapper(*fargs, **fkwargs):
        bound = _sig.bind(*args, *fargs, **kwargs, **fkwargs)
        return func(*bound.args, **bound.kwargs)
    return _wrapper

def test_mul_double_with_partial_standard_library():
    mul_double = partial(mul, 2)
    assert mul_double(5) == 10

def test_mul_double_with_my_partial():
    mul_double = _partial(mul, 2)
    assert mul_double(5) == 10
    mul_double = _partial(mul, y = 3)
    assert mul_double(5) == 15
    mul_double = _partial(mul, 2, y = 3)
    assert mul_double() == 6

if __name__ == '__main__':
    test_mul_double_with_partial_standard_library()
    test_mul_double_with_my_partial()
