#!/usr/bin/env python3
"""def de la clase Rectangle que hereda de BaseGeometry"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """triangulo definido por ancho y altura"""

    def __init__(self, width, height):
        """inicia un rectangulo validando sus dimensiones"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
