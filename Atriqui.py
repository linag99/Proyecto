board = [" | | ", " | | ", " | | "]
ganador = ""
    
def replace_string(s:str, i:int, j:str):
    s1 = s[0:i]
    s2 = s[i+1:]
    st = s1 + j + s2
    return st
    
def check_ganador():
    g = ""
    for i in range (len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not " " and board[0][i] is not "|":
            g = board[0][i]
    for i in range (len(board)):
        if board[i][0] == board[i][2] == board[i][4] and board[i][0] is not " "  and board[i][0] is not "|":
            g = board[i][0]
    if board[0][0] == board[1][2] == board[2][4] and board[0][0] is not " ":
        g = board[0][0]
    if board[0][4] == board[1][2] == board[2][0] and board[0][4] is not " ":
        g = board[0][4]
    return g
    
def empty_spaces():
    e = 9
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j] is not " " and board[i][j] is not "|":
                e -= 1
            
    return e

def jugar():
    jugador = input("¿Quien juega este turno? (X o O): ")
    fila = int(input("Escriba el numero de fila (1-3): "))
    pos = int(input("Escriba la posicion (1-3): "))
    if pos == 1:
        fpos = 0
    elif pos == 3:
        fpos = 4
    elif pos == 2:
        fpos = 2
    if (board[fila - 1][fpos] is " "):
        board[fila - 1] = replace_string(board[fila - 1], fpos, jugador.upper())
    else:
        print("Ya esta ocupado ese espacio.")
        print("")
    print(board[0])
    print(board[1])
    print(board[2])
    ganador = check_ganador()
    empty = empty_spaces()
    if ganador == "" and empty > 0:
        jugar()
    elif ganador is not "":
        print("El ganador es " + ganador + "!")
    elif empty <= 0:
        print("No hay ganador.")
        
        
print(board[0])
print(board[1])
print(board[2])
jugar()
