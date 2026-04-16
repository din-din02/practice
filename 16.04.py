from abc import ABC, abstractmethod
import math

class Fig(ABC):

    @abstractmethod
    def sqare(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Tre(Fig):
    def __init__(self, storona:int,  a:int, b:int):
        self.storona=storona
        self.a = a
        self.b = b

    def sqare(self) -> float:
        p=(self.storona+self.a+self.b)/2
        S=(p*(p-self.storona)*(p-self.a)*(p-self.b))**1/2
        return S

    def perimeter(self)->int:
        P = self.a + self.b + self.storona
        return P

class Pr(Fig):
    def __init__(self,storona:int,b:int):
        self.storona=storona
        self.b=b

    def sqare(self)->float:
        s=self.storona*self.b
        return s

    def perimeter(self)->float:
        p=(self.storona+self.b)*2
        return p

class Trapezia(Fig):
    def __init__(self,storona:int,h:int,a:int,c:int,d:int):
        self.storona=storona
        self.a=a
        self.h=h
        self.c=c
        self.d=d

    def sqare(self)->float:
        S1=((self.storona+self.a)/2)*self.h
        return S1
    def perimeter(self)->int:
        P1= self.a+self.storona+self.c+self.d
        return P1
    
class Circle(Fig):
    def __init__(self,r:int):
        self.r=r

    def sqare(self)->float:
        s1=3.14*self.r**2
        return s1
    def perimeter(self)->float:
        p1=2*3.14*self.r
        return p1

def func(*args):
    pass

def v():

    t=Tre(1,5,10)
    print(t.sqare())
    print(t.perimeter())
    p=Pr(29,4)
    print(p.sqare())
    print(p.perimeter())
    tr=Trapezia(1,2,3,4,5)
    print(tr.sqare())
    print(tr.perimeter())
    c=Circle(3)
    print(c.sqare())
    print(c.perimeter())

v()
