#!/usr/bin/env python3

"""modulo que define la clase Rectangle"""

class Rectangle:
    """representa un rectangulo"""
    def __init__(self, width=0, height=0):
        """inicia un rectangulo
        args:
        width (int): ancho 
        height (int): altura
        """

        self.width = width
        self.height = height

    @poperty
    def width(self):
        """ancho del rectangulo"""
        return self.__width

    @width.setter
    def width(self, value):
        """establece ancho del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @poperty
    def height(self):
        """alto del rectangulo"""
        return self.__height

    @height.setter
    def height(self, value):
        """establece alto del rectangulo"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

