#!/usr/bin/env python3
"""Este modulo define una clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """inicia un nuevo cuadrado"""

        self.__size = size

    @property
    def size(self):
        """recupera el tamano actual del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """establece un nuevo tamano"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calcula y devuelve el area del cuadrado"""

        return self.__size ** 2

    def my_print(self):
        """imprime el cuadrado"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print('#' * self.__size)
