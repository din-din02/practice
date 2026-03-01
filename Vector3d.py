class Vector3D:
    def __init__(self,x1,y1,z1,x2,y2,z2):
        self.x1=x1
        self.x2=x2
        self.z1=z1
        self.y1=y1
        self.y2=y2
        self.z2=z2

    def __str__(self):
        return(f"Координаты первого вектора:{self.x1,self.y1,self.z1}\nКоординаты второго вектора:{self.x2,self.y2,self.z2}")
    
    def cale (self):
        s=(self.x1*self.x2)+(self.y1*self.y2)+(self.z1*self.z2)
        print('Скалярное произведение векторов:', s)
        
        #Модули векторов
        a=(self.x1**2+self.y1**2+self.z1**2)**0.5
        b=(self.x2**2+self.y2**2+self.z2**2)**0.5
        #Cам косинус
        cos=s/(a*b)
        print('Угол между векторами:',cos)
        
        c=(a**2+b**2+2*a*b*cos)**0.5
        print('Длина третьего вектора:',c)
        
    def __del__(self):
        print('Удалено', self.x1, self.y1,self.z1,self.x2, self.y2,self.z2)

n=Vector3D(5,4,10,5,7,3)
print(n)
n.cale()
