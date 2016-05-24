import math
def areaCirculo():
    lado = int(input("Digite el lado del triangulo equilatero: "))
    altura = math.sqrt((lado**2)-((lado/2)**2))
    area = math.pi*((altura/3)**2)
    print ("El area de un circulo inscrito en un triangulo equilatero es :",area,)
    
areaCirculo()
