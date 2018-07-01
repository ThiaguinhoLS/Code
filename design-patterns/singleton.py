# -*- coding: utf-8 -*-

class Singleton(object):

    'Sempre retorna a mesma instância de Singleton'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


assert Singleton() is Singleton()


class Singleton(object):

    'Permite somente uma única referência a instância de Singleton'

    _instance = None

    def __init__(self, *args, **kwargs):
        if Singleton._instance != None:
            raise Exception('Class is Singleton')
        Singleton._instance = self

    @classmethod
    def get_instance(klass):
        if klass._instance == None:
            klass()
        return klass._instance
        

class Singleton(object):

    '''

    Implementação de um decorator para criação de classes Singleton
    
    Use assim:

    @Singleton
    class Point(object):

        pass
    
    '''

    def __init__(self, klass):
        self._klass = klass
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._klass(*args, **kwargs)
        return self._instance

from functools import wraps

def singleton(klass):

    'A parte ruim de utilizar um decorator para criar uma classe Singleton é a parte da documentação'
    
    _instance = None
    
    @wraps(klass)
    def wrapper(*args, **kwargs):
        if _instance is None:
            _instance = klass(*args, **kwargs)
        return _instance
    return wrapper


def singleton(klass):

    'Dessa forma retorno a própria classe ou seja a mesma não perde sua documentçao a não ser o método __new__'

    def _new(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(klass, cls).__new__(klass) # Passei klass, cls explicitamente
        return cls._instance

    klass.__new__ = _new
    return klass

