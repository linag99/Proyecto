def digitos():
    numero=int(input("Digite el número deseado: "))
    n = int(1)
    contar = int(10)

    while contar <= numero:
        n+=1
        contar = contar * 10
    print ("El número de cifras de "+str(numero)+" son "+str(n))
digitos()
        
    
    
