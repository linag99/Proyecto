#MiPong#

from tkinter import*

def pad1Arriba(r):
    c.move(pad1, 0, -10)
def pad1Abajo(r):
    c.move(pad1, 0, 10)

def pad2Arriba(e):
    c.move(pad2, 0, -10)
def pad2Abajo(e):
    c.move(pad2, 0, 10)

def moverBall():
    x1, y1, x2, y2 = c.coords(ball["obj"])
    x = (x1+x2)//2
    y = (y1+y2)//2
    dx = 4
    if x<10 or x>390:
        ball["dx"]*=-1
    if y<10 or y>390:
        ball["dy"]*=-1
    c.move(ball["obj"], ball["dx"], ball["dy"])
    ventana.after(50, moverBall)
    
ventana = Tk()
c = Canvas(ventana, width = 400, height=400)
c.pack()

c.create_line(200, 0, 200, 400)

pad1 = c.create_rectangle(10, 25, 20, 75, fill= "red")
pad2 = c.create_rectangle(380, 325, 390, 375, fill= "blue")
ball = {"dx": 5, "dy":5, "obj":c.create_oval(190, 190, 210, 210, fill= "black")}

ventana.bind("w", pad1Arriba)
ventana.bind("s", pad1Abajo)

ventana.bind("8", pad2Arriba)
ventana.bind("2", pad2Abajo)

ventana.after(10, moverBall)
