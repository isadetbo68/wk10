class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

class square(rectangle):
    def __init__(self, side):
        super().__init__(self, side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height

rect = rectangle(2, 3)
print("Resized rectangle area:", resize_rectangle(rect, 4, 5))  # Expected: 20
sq = square(4)
print("Resized square area:", resize_rectangle(sq, 5, 10))