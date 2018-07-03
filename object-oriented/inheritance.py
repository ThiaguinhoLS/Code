# -*- coding: utf-8 -*-

class Animal(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{__class__.__name__}(name = {name}, age = {age})'.format(__class__ = self.__class__, **self.__dict__)


class Dog(Animal):

    def __init__(self, name, owner): # Sobrescrita de método
        super().__init__(name) # Chamada ao método da classe base
        self.owner = owner # Definição de novo atributo

    def bark(self):
        print('{owner} mandou {name} latir!'.format(**self.__dict__))
        print('{name} Au! Au!'.format(name = self.name))
