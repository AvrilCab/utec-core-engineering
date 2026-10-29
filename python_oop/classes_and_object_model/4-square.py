#!/usr/bin/env python3
"""Este modulo define una clase Square con getters y setters"""


class Square:
    """Representa un cuadrado con tamano controlado por propiedades"""

    def __init__(self, size=0):
        """inicia un nuevo cuadrado

        Args:
             size (int): el tamano del cuadrado(por defecto 0)
        """

        self.__size = size

    @property
    def size(self):
        """recupera el tamano actual del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """establece un nuevo tamano para el cuadrado previa validacion"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calcula y devuelve el area del cuadrado"""

        return self.__size ** 2
