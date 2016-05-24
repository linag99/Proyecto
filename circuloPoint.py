import math
def circuloPoint():
    x =float(input("Digite la coordenada en x del punto de origen de la circunferencia: "))
    y =float(input("Digite la coordenada en y del punto de origen de la circunferencia: "))
    radio =float(input("Digite la medida del radio del circulo: "))
    xpu =float(input("Digite la coordenada del punto en x deseada a encontrar: "))
    ypu =float(input("Digite la coordenada del punto en y deseada a encontrar: "))
    if ((xpu-x)**2) + ((ypu-y)**2) < radio ** 2:
            point = "está dentro"
            print("El punto ", point, " de la circunferencia")
    elif ((xpu-x)**2) + ((ypu-y)**2) > radio ** 2:
            point = "está fuera"
            print("El punto ", point, " de la circunferencia")
    elif ((xpu-x)**2) + ((ypu-y)**2) == radio ** 2:
            point = "está en el borde"
            print("El punto ", point, " de la circunferencia")
     
circuloPoint()
