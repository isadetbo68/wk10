from abc import abstractmethod
class shape:
    @abstractmethod
    def area(self):
        pass    

class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def calculate_area(shape):
    return shape.area()