#!/usr/bin/env python3
"""
Modulo que define la clase Rectangle.
"""


class Rectangle:
    """
    Representa un rectangulo con ancho y alto definidos.
    """

    def __init__(self, width=0, height=0):
        """
        Inicializa un nuevo rectangulo.

        Args:
            width (int): Ancho del rectangulo (por defecto 0).
            height (int): Alto del rectangulo (por defecto 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectangulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectangulo con validacion de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectangulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto del rectangulo con validacion de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el area del rectangulo."""
        return self.width * self.height

    def perimeter(self):
        """Calcula y devuelve el perimetro del rectangulo."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
