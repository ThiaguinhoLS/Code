# -*- coding: utf-8 -*-
from functools import wraps

class _classmethod(object):

    def __init__(self, f):
        self.f = f

    def __get__(self, instance, klass = None):
        if klass is None:
            klass = self.__class__
        @wraps(self.f)
        def _wrapper(*args):
            return self.f(klass, *args)
        return _wrapper
        

def test_classmethod_decorator():

    class Spam(object):

        @_classmethod
        def grok(cls):
            return True

    assert Spam.grok() is True
    assert Spam().grok() is True


if __name__ == '__main__':
    test_classmethod_decorator()


