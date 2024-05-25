#!/usr/bin/python3
""" Square Class Module. """


class Square():
    """ A class representing a square. """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize a Square object with optional width and height. """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return a string representation of the square. """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a Square object. """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
