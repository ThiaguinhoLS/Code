# -*- coding: utf-8 -*-

class Memento(object):

    def __init__(self, content):
        self.content = content

    def save(self, file):
        return Memento(file.content)


class FileWrite(object):

    pass

