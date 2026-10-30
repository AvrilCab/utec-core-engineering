#!/usr/bin/env python3
"""def de la clase Square que hereda de Rectangle"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """representa un cuadrado"""

    def __init__(self, size):
        """inicia un cuadrado validando su tamano"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
       """devuelve la representacion del cuadrado en una cadena"""
       return f"[Square] {self.__size}/{self.__size}"
