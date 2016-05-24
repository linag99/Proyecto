import random as r

def generar_numero():
    n = ""
    while len(n) < 4:
        nn = r.randint(0, 9)
        if str(nn) not in n:
            n += str(nn)
    return n

numero = generar_numero()

def jugar():
    picas = 0
    famas = 0
    opcion = input("Introduzca un numero de cuatro cifras (sin repetirlas): ")
    if opcion != numero:
        for i in range (len(opcion)):
            for j in range (len(numero)):
                if (opcion[i] == numero[j]):
                    if i == j:
                        famas += 1
                    else:
                        picas += 1
        print("En " + opcion + " hay " + str(picas) + " picas y " + str(famas) + " famas.")
        jugar()
    else:
        print("Gano! El numero era " + opcion + ".")

jugar()
