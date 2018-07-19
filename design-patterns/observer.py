# -*- coding: utf-8 -*-

class Subject(object):

    def __init__(self):
        self._observers = set()

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.show(self.value)


class Formatter(Subject):

    'Formatador padrão somente retorna e redefine o valor'

    def __init__(self, value):
        super().__init__()
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError
        self._value = value
        self._notify()


class BinFormatter(object):

    'Converte os valores para binário'

    def show(self, value):
        print('Binary:', bin(value))


class HexFormatter(object):

    'Converte os valores para hexadecimal'

    def show(self, value):
        print('Hexadecimal:', hex(value))
