# -*- coding: utf-8 -*-
import doctest

class Person(object):

    '''

        Classe que modela uma pessoa com atributos name e age.
        name: str
        age: int
        Na teoria espero uma string para o nome e um inteiro para a idade mas não faço nenhuma verificação que confirme esses valores

    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '{__class__.__name__}(name = {name}, age = {age})'.format(__class__ = self.__class__, **self.__dict__)



class Person(object):

    ''' 
        Nesta classe faço asserções acerca dos valores passados ao inicializador verificando o tipo, isto funcionará somente no
        momento da instanciação do objeto não de suas atribuições
        
    '''

    def __init__(self, name, age):
        assert isinstance(name, str)
        assert isinstance(age, int)
        self.name = name
        self.age = age

    def __repr__(self):
        return '{__class__.__name__}(name = {name}, age = {age})'.format(__class__ = self.__class__, **self.__dict__)
    

    
if __name__ == '__main__':
    doctest.testmod()
