# -*- coding: utf-8 -*-
from contextlib import AbstractContextManager
from functools import partial

class FileOpener(AbstractContextManager):

    '''
    Implementação de um gerenciador de contexto utilizando como base a classe abstrata AbstractContextManager

    filename: Nome do arquivo
    mode: Mode de abertura do arquivo
    suppressed: Se True toda e qualquer exceção será suprimida, padrão é False

    Como usar:

    with FileOpener('file.txt', mode = 'w', suppressed = True) as f:
        f.write('Primeira linha\n')

    '''

    

    def __init__(self, filename, mode = 'r', *, suppress = False):
        self._opener = partial(open, filename, mode = mode)
        self._suppress = suppress

    def __enter__(self):
        self._file = self._opener()
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        return self._suppress

    

