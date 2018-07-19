# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import unittest

article = '''Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos, e vem sendo utilizado desde
o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos de tipos.
Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto para a editoração eletrônica ...'''

class AbstractInterface(ABC):

    @abstractmethod
    def show_article(self):
        pass


class FreeInterface(AbstractInterface):

    def show_article(self):
        return article[:50]


class PayInterface(AbstractInterface):

    def show_article(self):
        return article



class TestBridge(unittest.TestCase):

    def test_instantiate_abstractinterface_with_error(self):
        with self.assertRaises(TypeError):
            interface = AbstractInterface()

    def test_instantiate_freeinterface(self):
        interface = FreeInterface()
        self.

if __name__ == '__main__':
    unittest.main()
