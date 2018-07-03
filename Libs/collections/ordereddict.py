# -*- coding: utf-8 -*-
from collections import OrderedDict

class OrderedMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, dct):
        dct['__ordered__'] = [key for key in dct.keys() if not key.startswith('__')]
        return super().__new__(mcs, name, bases, dct)

class Spam(metaclass = OrderedMeta):

    a = 'A'
    b = 'B'

    def grok(self):
        pass


