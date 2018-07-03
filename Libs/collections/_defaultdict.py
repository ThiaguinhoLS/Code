# -*- coding: utf-8 -*-
from collections import defaultdict
import unittest

class _defaultdict(dict):

    def __init__(self, func = None):
        super().__init__()
        self.func = func

    def __getitem__(self, value):
        if not value in self:
            self.setdefault(value, self.func())
        return super().__getitem__(value)

    def __repr__(self):
        return '_defaultdict({}, {})'.format(self.func, super().__repr__())


class TestDefaultdict(unittest.TestCase):

    def test_instanciate_defaultdict(self):
        d = _defaultdict()
        self.assertEqual(repr(d), '_defaultdict(None, {})')

    def test_instanciate_with_list_class_defaultdict(self):
        d = _defaultdict(list)
        self.assertEqual(d['a'], [])

    def test_instanciate_with_int_class_defaultdict(self):
        d = _defaultdict(int)
        self.assertEqual(d['a'], 0)

    def test_instanciate_with_dict_class_defaultdict(self):
        d = _defaultdict(dict)
        self.assertEqual(d['a'], {})

    def test_int_append_defaultdict(self):
        d = _defaultdict(int)
        letters = ['a', 'b', 'c', 'a', 'b', 'a']
        for letter in letters:
            d[letter] += 1
        self.assertEqual(d, {'a': 3, 'b': 2, 'c': 1})

    def test_list_append_defaultdict(self):
        d = _defaultdict(list)
        data = (
            ('John', 'red'),
            ('Julie', 'yellow'),
            ('John', 'green'),
            ('Robert', 'blue'),
        )
        for owner, color in data:
            d[owner].append(color)
        self.assertEqual(d, {'John': ['red', 'green'], 'Julie': ['yellow'], 'Robert': ['blue']})


if __name__ == '__main__':
    unittest.main()
