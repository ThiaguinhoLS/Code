# -*- coding: utf-8 -*-
import unittest

class _Car(object):

    pass


class _Bike(object):

    pass


def factory_method(product_type):

    if product_type == 'car':
        return _Car()
    elif product_type == 'bike':
        return _Bike()
    else:
        raise ValueError('Cannot make: {}'.format(product_type))


class TestFactoryMethod(unittest.TestCase):

    'Testes'
    
    @unittest.skip('Ignore instanciate car')
    def test_instanciate_car(self):
        car = _Car()

    @unittest.skip('Ignore instanciate bike')
    def test_instanciate_bike(self):
        bike = _Bike()

    def test_factory_method_instanciate_a_car(self):
        car = factory_method('car')
        self.assertIsInstance(car, _Car)

    def test_factory_method_instanciate_a_bike(self):
        bike = factory_method('bike')
        self.assertIsInstance(bike, _Bike)


if __name__ == '__main__':
    unittest.main()
