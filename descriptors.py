# -*- coding: utf-8 -*-

class Descriptor(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point(object):

    x = Descriptor('x')
    y = Descriptor('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

