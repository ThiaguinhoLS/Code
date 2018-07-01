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



            

