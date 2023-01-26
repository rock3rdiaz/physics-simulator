from __future__ import annotations
from math import sqrt


class Custom2DVector:
    """
    Clase que representa un vector en 2 dimensiones.
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other: Custom2DVector):
        return Custom2DVector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: Custom2DVector):
        return Custom2DVector(
          self.x - other.x, self.y - other.y
        )

    def __mul__(self, value: float) -> Custom2DVector:
        return Custom2DVector(self.x * value, self.y * value)
    
    def __truediv__(self, value: float) -> Custom2DVector:
        return Custom2DVector(self.x / value, self.y / value)

    def norm(self) -> float:
        """
        Obtiene la norma del vector
        @return: norma del vector calculada
        """
        return sqrt((self.x ** 2) + (self.y ** 2))
