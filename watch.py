import turtle


hora = int(input("Digite la hora: "))
minuto = int(input("Digite los respectivos minutos: "))



def dibujarHora(hora:int):
    turtle.pencolor("red")
    turtle.right(hora*30)
    turtle.fd(57)
    turtle.fd(-57)
    turtle.left(hora*30)
def dibujarMinuto(minutos:int):
    turtle.pencolor("blue")
    turtle.right(minuto*6)
    turtle.fd(57)
    turtle.fd(-57)

turtle.setup(600,600)
turtle.left(180)
turtle.begin_fill()
turtle.fillcolor("pink")
turtle.circle(60,360)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.fd(57)
turtle.pendown()
turtle.right(90)
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(3,360)
turtle.end_fill()
turtle.right(90)
turtle.penup()
turtle.fd(-3)              
turtle.pendown()


dibujarHora(hora)
dibujarMinuto(minuto)



    

turtle.exitonclick()


              
            
              
              
              

