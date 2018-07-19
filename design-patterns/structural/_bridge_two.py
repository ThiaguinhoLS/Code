class Circle:
    
    class DrawingAPIOne:
            '''Implementation-specific abstraction'''
            def drawCircle(self, x, y, radius):
                    print("API 1 is drawing a circle at ({}, {}) with radius {}".format(x, y, radius))
                    
    class DrawingAPITwo:
            '''Implementation-specific abstraction'''
            def drawCircle(self, x, y, radius):
                    print("API 2 is drawing a circle at ({}, {}) with radius {}".format(x, y, radius))
                     
    def __init__(self, x, y, radius):
            '''Implementation-independent abstraction; Initialize the necessary attributes'''
            self._x = x
            self._y = y
            self._radius = radius
            
    def drawWithAPIOne(self):
            '''Implementation-specific abstraction'''
            objectOfAPIone = self.DrawingAPIOne()
            objectOfAPIone.drawCircle(self._x, self._y, self._radius)
            
    def drawWithAPITwo(self):
            '''Implementation-specific abstraction'''
            objectOfAPItwo = self.DrawingAPITwo()
            objectOfAPItwo.drawCircle(self._x, self._y, self._radius)
            
    def scale(self, percent):
            '''Implementation-independent abstraction'''
            self._radius *= percent

# Instantiate a circle
circle1 = Circle(0, 0, 2)
# Draw it using API One
circle1.drawWithAPIOne()
 
# Instantiate another circle
circle2 = Circle(1, 3, 3)
# Draw it using API Two
circle2.drawWithAPITwo()
 
