# -*- coding: utf-8 -*-
import unittest

class deque(list):

    def __init__(self, iterable, *, maxlen = None):
        super().__init__(iterable[:maxlen])
        self.maxlen = maxlen

    def _verify(self):
        if self.maxlen is not None:
            if len(self) >= self.maxlen:
                return True

    def append(self, value):
        if self._verify() is True:
            self.popleft()
        super().append(value)

    def popleft(self):
        return self.pop(0)

    def appendleft(self, value):
        if self._verify() is True:
                self.pop()
        self.insert(0, value)


class TestDeque(unittest.TestCase):

    def test_instanciate_deque(self):
        d = deque([1, 2, 3])
        self.assertEqual(d, [1, 2, 3])

    def test_maxlen_attribute_deque(self):
        d = deque([1, 2, 3], maxlen = 2)
        self.assertEqual(d, [1, 2])

    def test_method_append_deque(self):
        d = deque([1, 2, 3])
        d.append(4)
        self.assertEqual(d, [1, 2, 3, 4])

    def test_method_popleft_deque(self):
        d = deque([1, 2, 3])
        value = d.popleft()
        self.assertEqual(value, 1)
        self.assertEqual(d, [2, 3])

    def test_method_appendleft(self):
        d = deque([1, 2, 3])
        d.appendleft(0)
        self.assertEqual(d, [0, 1, 2, 3])

    def test_method_append_with_maxlen_deque(self):
        d = deque([1, 2, 3], maxlen = 3)
        d.append(4)
        self.assertEqual(d, [2, 3, 4])

    def test_method_appendleft_with_maxlen_deque(self):
        d = deque([1, 2, 3], maxlen = 3)
        d.appendleft(0)
        self.assertEqual(d, [0, 1, 2])
        

if __name__ == '__main__':
    unittest.main()
