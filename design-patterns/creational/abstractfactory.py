# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import unittest
import random

class PolygonFactory(ABC):

    @classmethod
    def make(cls):
        products = []
        module = __import__(__name__)
        name = random.choice(cls.products)
        type_class = getattr(module, name)
        for n in range(random.randint(1, 3)):
            product = type_class(cls.__name__)
            products.append(product)
        return products


class TriangleFactory(PolygonFactory):

    products = ['TriangleIsosceles', 'TriangleEquilateral', 'TriangleScalene']

    pass
        


class QuadrilateralFactory(PolygonFactory):

    products = ['Square', 'Rectangle']

    pass


class Polygon(ABC):

    def __init__(self, factory_name):
        self._factory_name = factory_name

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass
    
    @property
    def manufactured(self):
        return self._factory_name

    
class Triangle(Polygon):

    @property
    def perimeter(self):
        return 'a+b+c'

    @property
    def area(self):
        return 'b*h/2'


class TriangleIsosceles(Triangle):

    @property
    def perimeter(self):
        return '2a+b'


class TriangleEquilateral(Triangle):

    @property
    def perimeter(self):
        return '3a'


class TriangleScalene(Triangle):

    pass


class Quadrilateral(Polygon):

    @property
    def perimeter(self):
        return 'a+a+a+a'

    @property
    def area(self):
        return 'a*a'


class Square(Quadrilateral):

    pass


class Rectangle(Quadrilateral):

    @property
    def area(self):
        return 'a*b'


def give_me(factory):
    return factory.make()


class TestAbstractFactory(unittest.TestCase):

    def test_instantiate_factory_class_triangle_no_error(self):
        factory = TriangleFactory()
        self.assertIsInstance(factory, PolygonFactory)

    def test_instantiate_factory_class_quadrilateral(self):
        factory = QuadrilateralFactory()
        self.assertIsInstance(factory, PolygonFactory)

    def test_instantiate_using_triangle_factory_length(self):
        triangles = give_me(TriangleFactory)
        self.assertGreater(len(triangles), 0)

    def test_instantiate_using_triangle_factory(self):
        triangles = give_me(TriangleFactory)
        for triangle in triangles:
            with self.subTest(triangle = triangle):
                self.assertIsInstance(triangle, Triangle)

    def test_instantiate_using_quadrilateral_factory_length(self):
        quadrilaterals = give_me(QuadrilateralFactory)
        self.assertGreater(len(quadrilaterals), 0)

    def test_instantiate_using_quadrilateral_factory(self):
        quadrilaterals = give_me(QuadrilateralFactory)
        for quadrilateral in quadrilaterals:
            with self.subTest(quadrilateral = quadrilateral):
                self.assertIsInstance(quadrilateral, Quadrilateral)


if __name__ == '__main__':
    unittest.main()
