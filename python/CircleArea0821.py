def Area(r):
    pi=3.14159265358
    return ((r**2)*pi)
def Prei(r):
    pi=3.14159265358
    return ((2*r)*pi)
def SphereArea(r):
    pi=3.14159265358
    return (4*pi*r**2)
R=float(input('r='))
A=Area(R)
B=Prei(R)
C=SphereArea(R)
print('Area=',A)
print('Prei=',B)
print('SphereArea=',C)