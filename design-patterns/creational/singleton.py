# -*- coding: utf-8 -*-
import unittest
from abc import ABC

class Singleton(ABC):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class Spam(Singleton):

    pass


class TestSingleton(unittest.TestCase):

    def test_instantiate_spam_verify_isinstance(self):
        spam = Spam()
        self.assertIsInstance(spam, Singleton)

    def test_spam_instances_is_same(self):
        self.assertEqual(id(Spam()), id(Spam()))

if __name__ == '__main__':
    unittest.main()
