# -*- coding: utf-8 -*-

from functools import partial

class FileOpener(object):

    def __init__(self, filename, mode = 'w'):
        self._opener = partial(open, filename, mode = mode)

    def __enter__(self):
        self.file = self._opener()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        'Se quiser suprimir uma exceção levantada no gerenciador de contexto basta retorna True caso contrário a mesma será'
        ' propagadada'
        self.file.close()
        

with FileOpener('file.txt') as f:
    f.write('Primeira linha\n')
