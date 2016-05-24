

hora = int(input("Digite la hora: "))
minuto = int(input("Digite los respectivos minutos: "))


def calcularAngulo():
    angulo = ((hora*30)+(minuto*0.5))-(minuto*6)
    return angulo

print("El angulo que marcan las manecillas del reloj es :", calcularAngulo(),)

calcularAngulo()
