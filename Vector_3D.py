import math
from Vector_2D import Vector2D


class Vector3D(Vector2D):
    def __init__(self, x=0.0 , y=0.0 , z = 0.0):
        super().__init__(x, y)
        self._z = z
        

    def __str__(self):
        return f"Vector3D({self._x}, {self._y}, {self._z})"  
    
    def __add__(self, other):
        return Vector3D(self._x + other._x, self._y + other._y, self._z + other._z)
    
    def __sub__(self, other):
        return Vector3D(self._x - other._x, self._y - other._y, self._z - other._z)
    
    def __mul__(self, scalar):
        return Vector3D(self._x * scalar, self._y * scalar, self._z * scalar)
    
    def length(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)
    

v1 = Vector2D(3,1)
v2 = Vector2D(2,4)
v7 = Vector3D(1,2,3)
v8 = Vector3D(3,2,1)

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 3
v6 = v1.length()
print("Сложение",v3)
print("Разность",v4)
print("Домножить на число 3",v5)
print("Длина",v6)


v9 = v7 + v8
v10 = v7 - v8
v11 = v7 * 3
v12 = v7.length()
print("Сложение",v9)
print("Разность",v10)
print("Домножить на число 3",v11)
print("Длина",v12)
