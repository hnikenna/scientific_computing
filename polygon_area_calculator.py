class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for line in range(self.height):
                for char in range(self.width):
                    picture += '*'
                picture += '\n'
            return picture

    def get_amount_inside(self, shape):
        count = int(self.get_area() / shape.get_area())
        return count

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(width=side, height=side)
        self.side = side

    def set_side(self, side):
        self.side = side
        super(Square, self).__init__(width=self.side, height=self.side)

    def set_width(self, width):
        self.side = width
        super(Square, self).__init__(width=self.side, height=self.side)

    def set_height(self, height):
        self.side = height
        super(Square, self).__init__(width=self.side, height=self.side)

    def __str__(self):
        return f'Square(side={self.side})'

