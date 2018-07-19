# -*- coding: utf-8 -*-
'''
Boleanos(True, False) -> Verdade ou Falso
Números(int, float) -> Inteiros, Ponto flutuante, frações e até números complexos
Strings(str) -> Sequências de caracteres
Bytes e bytes arrays(bytes) -> Uma imagem JPEG
Listas(list) -> Sequências ordenadas de valores
Tuplas(tuple) -> Sequências ordenadas e imutáveis de valores
Conjuntos(set) -> Pacotes não ordenadas de elementos únicos
Dicionários(dict) -> Pacotes não ordenados de pares chave-valor

'''

class ListInt(list):

    def __init__(self, iterable = None):
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Value "{value}" is not int')
        super().append(value)

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def insert(self, index, value):
        if not isinstance(value, (list, tuple)):
            value = [value]
        for item in value:
            self.append(value)

    def __getitem__(self, index):
        print(index)
        return super().__getitem__(index)
    
