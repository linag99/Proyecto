def Potencia(n:int, x:int):
    i=n
    t=n
    if(x==0):
        return 1
    for h in range (1, x):
        t=0
        for s in range(n):
            t+=i
        i=t
    return t
