# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Product(object):

    'Classe que modela um produto'

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f'"{value}" preço não é um número válido')
        self._price = value

    def calculate_send(self, send):
        return send.calculate(self.price)

    
class AbstractSend(ABC):

    'Classe abstrata que modela uma forma de envio o método calculate é abstrato logo deve ser sobrescrito nas subclasses'

    @staticmethod
    @abstractmethod
    def calculate(value):
        pass


class Sedex(AbstractSend):

    'Modela um forma de envio de produtos'

    @staticmethod
    def calculate(value):
        return value * 10


class Pac(AbstractSend):
    
    'Modela um forma de envio de produtos'

    @staticmethod
    def calculate(value):
        return value * 5


def get_name():
    'Retorna a entrada para o nome do produto'
    return input('Digite o nome do produto: ')


def get_price():
    'Retorna a entrada para o preço do produto'
    return float(input('Digite o preço do produto: '))


def add_product(product):
    'Adiciona um único produto'
    products.append(product)
    print('Adicionado com sucesso')


def show_product(product):
    'Mostra as informações de um produto específico'
    print(f'Nome: {product.name}\nPreço: R$ {product.price:.2f}')


def list_products():
    'Lista todos os podutos'
    if products:
        print('{:-^50}'.format('Lista de produtos'))
        for product in products:
            show_product(product.name, product.price)
    else:
        print('Nenhum produto na lista')


def calculate_price(product, send):
    'Calcula o preço do envio de um produto específico'
    print('{:-^50}'.format('Calculando preço'))
    return product.calculate_send(send)


def decorator(func):
    pass

products = []

options = (
        ('Sair', None),
        ('Adicionar produto', add_product),
        ('Listar produtos', list_products),
        ('Calcular preço', calculate_price),
    )


def main():
    while True:
        for number, option in enumerate(options):
            print(f'[{number}] - {option[0]}')
        try:
            choice = int(input('Escolha uma opção: '))
            if not choice:
                break
            options[choice][1]()
        except ValueError as exc:
            pass


if __name__ == '__main__':
    main()
    



