import random as r

palabras = ["rinoceronte", "maleta", "lluvia", "llenar", "particion", "yuxtaposicion", "amoeba", "virulento", "cartera", "formula", "cateter", "catatonico"]
espacios = ""
palabra = ""
letras = []
intentos = 10

def replace_string(s:str, i:int, j:str):
    s1 = s[0:i]
    s2 = s[i+1:]
    st = s1 + j + s2
    return st

def hallar_palabra():
    n = 0
    for i in range (len(palabras)):
        n+=1
    p = r.randint(0, n-1)
    return palabras[p]

palabra = hallar_palabra()

def esp(l:str):
    n = 0
    for i in range (len(palabra)):
        n += 1
    return n

espacios = esp(palabra)
string = "_"*espacios

def ya_escogida(l:str):
    for i in range (len(palabra)):
        if len(letras) > 0:
            for j in range (len(letras)):
                if (letras[j] == l):
                    return True
    return False

def jugar():
    real = palabra
    global intentos
    if real != string.lower():
        if intentos > 0:
            letra = input("Escoja una letra: ")
            if ya_escogida(letra):
                print("Esa letra ya fue usada.")
                jugar()
            else:
                letras.append(letra)
                chequeo = 0
                for i in range (len(palabra)):
                    if letra == palabra[i]:
                        global string
                        string = replace_string(string, i, letra.upper())
                    else:
                        chequeo += 1
                if chequeo == len(palabra):
                    intentos -= 1
                    print("La letra no esta. Intentos restantes: " + str(intentos))
                print(string)
                jugar()
        else:
            print("No mas intentos! Juego terminando. Usted perdió.")
    else:
        print("Gano! La palabra era '" + palabra + "'.")

print(string)
jugar()