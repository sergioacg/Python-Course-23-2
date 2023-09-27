
from math import pi

#Vamos a generar una clase abstracta
#Es una clase que no puede instanciar un objeto directamente
#sino que debe haerlo a través de otra clase (Molde)
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    #Polimorfismo
    #Cambiar el comportamiento de la clase padre
    #area - > cambiar ese compoirtamiento
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width  +  self.height)
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

if __name__ == '__main__':
    figura = Shape()
    print(figura.area())

    shapes = [Rectangle(3, 2),  Circle(4),  Square(4)]
    for shape in shapes:
        print(f'Area: {shape.area():2.2f}\nPerimeter: {shape.perimeter():2.2f}\n\n')


