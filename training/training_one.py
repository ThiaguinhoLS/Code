# -*- coding: utf-8 -*-

from collections import namedtuple

class Line(namedtuple('Point', ['x', 'y'])):

    __slots__ = ()


class ImmutableObject(object):

    'Possui algumas falhas como poder definir atributos da seguinte forma: obj.__dict__[attrname] = value'

    def __init__(self, a, b):
        object.__setattr__(self, 'a', a)
        object.__setattr__(self, 'b', b)

    def __setattr__(self, attrname, value):
        raise AttributeError('{__class__.__name__} não possui atributo "{attrname}"'.format(__class__ = self.__class__,
                                                                                          attrname = attrname))

class ImmutableTuple(tuple):

    __slots__ = ()

    def __new__(cls, a, b):
        return tuple.__new__(cls, (a, b))

    def __getattr__(self, attrname):
        if attrname == 'a':
            return self[0]
        elif attrname == 'b':
            return self[1]
        raise AttributeError(f'{attrname} não está definido')

    def __setattr__(self, attrname, value):
        raise TypeError('Classe imutável')



for i in range(1, 10): print(i) if i % 2 == 0 else print('Não')
