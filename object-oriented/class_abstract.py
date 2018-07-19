# -*- coding: utf-8 -*-

class Abstract(object):

    def grok(self):
        return NotImplemented


class Concret(Abstract):

    def grok(self):
        # do something
        pass


from abc import ABC, abstractmethod

class Abstract(ABC):

    'Define uma classe abstrata'

    @abstractmethod
    def grok(self):
        # Método abstrato deve ser sobrescrito o irá leventar uma exceção'
        pass


class Concret(Abstract):

    def grok(self):
        # do something
        pass

