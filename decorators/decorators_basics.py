# -*- coding: utf-8 -*-

def decorator(func):
    'Pelo decorator retornar outra função diferente da decorada perdemos alguns atributos para instrospecção como o __doc__'
    def wrapper(x, y):
        return func(x, y)
    return wrapper

@decorator
def add(x, y):
    'Função que adiciona dois números'
    return x + y


from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(x, y):
        return func(x, y)
    return wrapper


def sub(x, y):
    'Função que subtrai 2 números'
    return x - y


def initialize_once(func):
    'Executa a função uma única vez'
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal called
        if not called:
            called = True
            return func(*args, **kwargs)
    called = False
    return wrapper


@initialize_once
def print_message(message):
    print(message)


def count_called(func):
    'Conta quantas vezes a função decorada foi chamada'
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper._count += 1
        return func(*args, **kwargs)
    wrapper._count = 0
    return wrapper

        
@count_called
def double(x):
    return x * 2


def memoize(func):
    'Função que memoriza valores de chamada e resultados evitando chamadas a função decorada caso o resulta esteja salvo'
    _cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper


@memoize
def mul(x, y):
    return x * y


