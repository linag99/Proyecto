def valorB():
    numper = int(input("Digite el número de personas"))
    plan = int(input("Escoja el numero de plan, 1 o 2"))
    tempo = str(input("Elija la temporada, alta o baja"))
    if numper>0 and plan==1 and tempo=="alta":
        valor = ((numper*480000)*0.1)+(numper*480000)
    if numper>0 and plan==1 and tempo=="baja":
        valor = ((numper*384000)*0.1)+(numper*384000)
    if numper>0 and plan==2 and tempo=="alta":
        valor = int((numper*650000)*0.1)+(numper*650000)
    if numper>0 and plan==2 and tempo=="baja":
        valor = ((numper*455000)*0.1)+(numper*455000)
    return valor
print ("Su valor de la estadia es ", valorB())


