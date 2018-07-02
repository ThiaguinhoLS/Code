# -*- coding: utf-8 -*-
from contextlib import contextmanager
import os

@contextmanager
def change_path(path):
    '''

        Altera o path atual e depois do fechamento do contexto retorna o path
        Como usar:
        with change_path('../'):
            do something

    '''
    actual = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(actual)


