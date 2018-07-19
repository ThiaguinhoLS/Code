# -*- coding: utf-8 -*-
import unittest

class Suit(object):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return '{__class__.__name__}(name = {name}, symbol = {symbol})'.format(__class__ = self.__class__, **self.__dict__)

    def __str__(self):
        return self.symbol


Spades, Hearts, Diamonds, Clubs = Suit('Spades', '♠'), Suit('Hearts', '♥'), Suit('Diamonds', '♦'), Suit('Clubs', '♣')


class Card(object):

    'Representação do objeto em si'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{__class__.__name__}(rank = {rank}, suit = {suit})'.format(__class__ = self.__class__, **self.__dict__)

    def __str__(self):
        return '{rank}{suit}'.format(**self.__dict__)


def factory(rank, suit):
    
    'Lógica de criação do objeto num único lugar'
    
    if rank == 1:
        return Card('A', suit)
    elif rank == 11:
        return Card('J', suit)
    elif rank == 12:
        return Card('Q', suit)
    elif rank == 13:
        return Card('K', suit)
    raise ValueError('Card rank is not valid')


def factory(rank, suit):

    'Lógica de criação do objeto num único lugar'

    rank_card = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}

    if rank in rank_card:
        return Card(rank_card.get(rank), suit)
    elif rank > 2 and rank < 11:
        return Card(rank, suit)
    raise ValueError('Card rank is not valid')
    


class TestFactory(unittest.TestCase):

    'Testes da fábrica de objetos'

    def test_instanciate_one_card_suit_spades(self):
        card = factory(1, Spades)
        self.assertEqual(str(card), 'A♠')

    def test_instanciate_one_card_suit_hearts(self):
        card = factory(1, Hearts)
        self.assertEqual(str(card), 'A♥')

    def test_instanciate_one_card_suit_diamonds(self):
        card = factory(1, Diamonds)
        self.assertEqual(str(card), 'A♦')

    def test_instanciate_one_card_suit_clubs(self):
        card = factory(1, Clubs)
        self.assertEqual(str(card), 'A♣')

    def test_repr_card(self):
        card = factory(1, Clubs)
        self.assertEqual(repr(card), 'Card(rank = A, suit = ♣)')

    def test_instanciate_one_card_with_letters_in_rank_eleven(self):
        card = factory(11, Spades)
        self.assertEqual(str(card), 'J♠')

    def test_instanciate_one_card_with_letters_in_rank_twelve(self):
        card = factory(12, Hearts)
        self.assertEqual(str(card), 'Q♥')

    def test_instanciate_one_card_with_letters_in_rank_thirteen(self):
        card = factory(13, Diamonds)
        self.assertEqual(str(card), 'K♦')

    def test_instanciate_one_card_with_error_in_rank_eleved(self):
        with self.assertRaises(ValueError):
            card = factory(14, Clubs)

    def test_instanciate_one_card_with_errorin_rank(self):
        with self.assertRaises(ValueError):
            card = factory(0, Clubs)


if __name__ == '__main__':
    unittest.main()

