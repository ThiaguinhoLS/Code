# -*- coding: utf-8 -*-

class Piece(object):

    def move(self):
        raise NotImplemented()

    
class _Horse(Piece):

    def move(self):
        return 'I move in L'


class _Bishop(Piece):

    def move(self):
        return 'I move in diagonally'


def factory_method(piece_name):

    types_pieces = {'horse': _Horse, 'bishop': _Bishop}
    klass = types_pieces.get(piece_name)
    if not klass:
        raise ValueError(f'"{piece_name}" is not valid name for piece')
    return klass()


def main():
    piece_one = factory_method('horse')
    print(piece_one.move()) # 'I move in L'
    piece_two = factory_method('bishop')
    print(piece_two.move()) # 'I move in diagonally'


if __name__ == '__main__':
    main()
