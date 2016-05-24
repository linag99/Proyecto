#Lina María Guerra
#Tarea de máximos y mínimos
import math
def minMax():
    ecu = input("Digite la ecuación a evaluar: ")
    y=int(input("Digite el número de puntos con los que desea buscar el mínimo y el máximo"))
    x=0
    n=1/y
    mini = 999999999
    maxi = -999999999
    while x<=1:
        R = eval(ecu)
        maxi = max(maxi,R)
        mini = min(mini,R)
        x+=n
    print("En el intervalo de [0,1], el máximo de la ecuación dada es:", maxi," y el mínimo es:",mini)
minMax()
