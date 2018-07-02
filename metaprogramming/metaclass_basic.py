# -*- coding: utf-8 -*-
import os   

class Metaclass(type):

    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        if not os.path.exists(name):
            os.makedirs(name)
        return cls

class Product(metaclass = Metaclass):

    products = []

    def __new__(cls, *args):
        obj = super().__new__(cls)
        return obj

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._save()

    def _save(self):
        self.__class__.products.append(self.name + ':' + str(self.price) + '\n')

    @classmethod
    def write(cls):
        file = open(os.path.join(cls.__name__, '_data'), 'w')
        file.writelines(cls.products)
        file.close()

