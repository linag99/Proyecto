from math import sqrt
def cuadrativaP(a:float, b:float, c:float) -> float:
x = (-b + sqrt(b**2-4ac))/(2*a)
return x

def cuadrativaN(a:float, b:float, c:float) -> float:
x = (-b - sqrt(b**2-4ac))/(2*a)
return x

print(cuadraticaP(-0.5,2,5), cuadraticaN(-0.5,2,5))
