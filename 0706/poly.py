class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
 
shapeList = [Circle(5), Rectangle(4, 6)]
for shape in shapeList:
    print(f"{shape.name} area: {shape.area()}")               