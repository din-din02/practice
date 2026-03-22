import math


class Vector2D():
    def __init__(self, x = 0.0, y = 0.0):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Vector2D ({self._x}, {self._y})"
    
    def __add__(self, other):
        return Vector2D(self._x + other._x, self._y + other._y)
    
    def __sub__(self, other):
        return Vector2D(self._x - other._x, self._y - other._y)
    
    def __mul__(self, scalar):
        return Vector2D(self._x * scalar, self._y * scalar)
    
    def length(self):
        return math.sqrt(self._x**2 + self._y**2)
    
