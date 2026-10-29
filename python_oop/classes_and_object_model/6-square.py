#!/usr/bin/env python3
"""Este modulo define una clase Square"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size=0, position=(0, 0)):
        """inicia un nuevo cuadrado"""

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """obtiene la posicion del cuadrado"""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posicion cuadrado."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """calcula y devuelve el area del cuadrado"""

        return self.__size ** 2

    def my_print(self):
        """imprime el cuadrado"""
        print(self.__str__())

    def __str__(self):
        """define la represenacion en cdena del cuadrado"""
        if self.__size == 0:
            return ""

        square_sr = []
        square_str.append("\n" + self.position[1])

        for i in range(self.__size):
            square_str.append(" " * self.__position[0] + "#" * self.__size)
            if i < self.__size - 1:
                square_str.append("\n")

        return "".join(square_str)
