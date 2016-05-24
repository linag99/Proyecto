def primos(numero:int)->bool:
    if (numero==1 or numero==2 or numero ==3 or numero==7):
        return True
    for i in range(2,10):
        if (numero%i)==0:
            return False
    return True


def digPrimos(numero:int):
    n = 0
    i=2
    while (n<numero):
        if (primos(i)):
            print (str(i),end=",")
            n+=1
        i+=1
    return
