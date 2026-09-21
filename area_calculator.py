class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return f"el area es:{self.width * self.height}"

    def get_perimeter(self):
        return f"el perimetro es:{2 * self.width + 2 * self.height}"

    def get_diagonal(self):
        return f"la diagonal es:{(self.width ** 2 + self.height ** 2) ** 0.5}"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return f"la imagen es:\n{('*' * self.width + '\n') * self.height}"

    def get_amount_inside(self, shape):
        return f"la cantidad que entra es:{(self.width // shape.width) * (self.height // shape.height)}"

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"

rectangulo = Rectangle(49, 2)
print(rectangulo.get_area())  
print(rectangulo.get_perimeter()) 
print(rectangulo.get_diagonal())  
print(rectangulo.get_picture())