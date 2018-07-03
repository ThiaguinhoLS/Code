# -*- coding: utf-8 -*-

class A(object):

    def grok(self):
        return 'A'


class B(object):

    def grok(self):
        return 'B'


class C(A, B):

    pass


class D(B, A):

    pass


assert C().grok() == 'A'
assert D().grok() == 'B'
