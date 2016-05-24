def triPascal():
    #imprime el numero de lineas del triangulo de pascal
    num =int(input("Dígite el número de lineas")) 
    p = 0 
    q = 0 
    import math 
    while (p<=num): 
        print( ' ' ) 
        print( ' ' ) 
        while(q<=p): 
            r=p-q 
            n=math.factorial(r) 
            t=math.factorial(q) 
            p1=math.factorial(p) 
            q1=n*t 
            rta=p1//q1 
            q+=1 
            print ( rta , end=' ') 
        p=p+1 
        q=0
triPascal()
print( ' ' )
print( ' ' )
while(True):
    m = input("¿Desea hacer otro triángulo?")
    
    if (m=="si"):
        triPascal()
        print("  <--Toma tu triangulo", )
        
    else:
        print("Adiós :'(")
        break
    
