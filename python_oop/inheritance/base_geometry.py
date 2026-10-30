#!/usr/bin/env python3

"""definicion de la clase BaseGeometry"""


class BaseGeometry:
    """clase para geometria y validaciones"""

    def area(self):
        """calcula el area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valida que un valor sea un entero positivo > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
