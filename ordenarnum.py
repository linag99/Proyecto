def ordenar ():
    "ordena los números de menor a mayor"
    a =int(input("Dígite el primer número a ordenar:"))
    b =int(input("Dígite el segundo número a ordenar:"))
    c =int(input("Dígite el tercer número a ordenar:"))
    if a >= b >= c:
            print("El orden es: ", a, b, c)
    if c > a >= b:
            print("El orden es: ", c, a, b)
    if b > a >= c:
            print("El orden es: ", b, a, c)
    if a > c > b: 
            print("El orden es: ", a, c, b)
    if c > b > a:
            print("El orden es: ", c, b, a)
    if b > c > a:
            print("El orden es: ", b, c, a)
    
            
ordenar()

while(True):
    s = input("¿Quieres seguir ordenando?")
    if (s=="Si"):
        print(ordenar())

    else:
        exit()  


