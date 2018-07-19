# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Director(object):

    'Classe que implementa a sequência de criação da classe'

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.construct_part_a()
        self._builder.construct_part_b()


class AbstractBuilder(ABC):

    @abstractmethod
    def construct_part_a(self):
        pass

    @abstractmethod
    def construct_part_b(self):
        pass


class ConcreteBuilder(AbstractBuilder):

    def construct_part_a(self):
        pass

    def construct_part_b(self):
        pass


    
