#!/usr/bin/env python3
"""Este modulo define una clase Square con calculo de area"""


class Square:
    """Representa un cuadrado con validaciones de tamano y calculo de area"""

    def __init__(self, size=0):
        """inicia un nuevo cuadrado

        Args:
             size (int): el tamano del cuadrado(por defecto 0)

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """calcula y devuelve el area del cuadrado"""

        return self.__size ** 2 
