# -*- coding: utf-8 -*-

class _staticmethod(object):

    def __init__(self, f):
        self.f = f

    def __get__(self, instance, klass = None):
        return self.f


def test_staticmethod_decorator():

    class Spam(object):

        @_staticmethod
        def grok(value):
            return value

    assert Spam.grok(2) == 2
    assert Spam().grok(2) == 2


if __name__ == '__main__':
    test_staticmethod_decorator()
    
