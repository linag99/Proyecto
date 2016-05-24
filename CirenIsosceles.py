import math
def areaCirculo():
    lado = int(input("Digite el lado igual del triangulo isosceles: "))
    altura = math.sqrt((lado**2)-((lado**2)/4))
    area = math.pi*((altura/3)**2)
    print ("El area de un circulo inscrito en un triangulo isosceles es :",area,)
    
areaCirculo()
