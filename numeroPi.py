def numeroPi(n:int)-> float:
    i=1
    p=0
    sign=1
    counter=0
    while(counter<n):
        p+=(1/i)*sign
        sign=sign*-1
        i+=2
        counter+=1
    return p*4
    
    
