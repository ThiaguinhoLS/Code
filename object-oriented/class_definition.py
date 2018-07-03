# -*- coding: utf-8 -*-

class Point(object): # object a última classe na hieraquia de classes

    def __init__(self, x, y):
        'Método inicializador'
        self.x = x # Defininado atributos de instância
        self.y = y

    def __repr__(self):
        'Método de representação do objeto'
        return '{__class__.__name__}(x = {x}, y = {y})'.format(__class__ = self.__class__, **self.__dict__)

