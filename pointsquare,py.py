def cuadradoPoint():
    x =float(input("Digite la coordenada en x del punto de inicio del cuadrado: "))
    y =float(input("Digite la coordenada en y del punto de inicio del cuadrado: "))
    lado =float(input("Digite la medida del lado del cuadrado: "))
    xpu =float(input("Digite la coordenada del punto en x deseada a encontrar: "))
    ypu =float(input("Digite la coordenada del punto en y deseada a encontrar: "))
    xx = x+lado
    yy = y+lado
    point = "está afuera"
    if (xpu > x and xpu < xx) and (ypu > y and ypu < yy):
            point = "está adentro"
            print("El punto ", point, " del cuadrado")
    if ((xpu == x or xpu == xx) and (ypu >= y and ypu <= yy)) or ((xpu >= x and xpu <= xx) and (ypu == y or ypu == yy)):
            point = "está en el borde"
            print("El punto ", point, " del cuadrado")

cuadradoPoint()         
