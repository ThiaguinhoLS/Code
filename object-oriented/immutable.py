# -*- coding: utf-8 -*-
import unittest

class Immutable(tuple):

    'Criação de classe imutável utilizando o construtor da tupla'

    def __new__(cls, a, b):
        return tuple.__new__(cls, (a, b))

    def __getattr__(self, attrname):
        if attrname == 'a':
            return self[0]
        elif attrname == 'b':
            return self[1]
        raise AttributeError(f'{attrname} is not defined')

    def __setattr__(self, attrname, value):
        raise NotImplementedError('Class is immutable')

    
class TestImmutable(unittest.TestCase):

    'Testes da classe Immutable'

    def setUp(self):
        self.immutable = Immutable(1, 2)

    def test_access_attributes(self):
        self.assertEqual(self.immutable.a, 1)
        self.assertEqual(self.immutable.b, 2)

    def test_error_access_attribute_not_defined(self):
        with self.assertRaises(AttributeError) as exc:
            self.immutable.c

    def test_error_set_attribute(self):
        with self.assertRaises(NotImplementedError) as exc:
            self.immutable.c = 3
            

if __name__ == '__main__':
    unittest.main()
