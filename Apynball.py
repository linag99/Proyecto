from tkinter import*
import time
import random

def mostrar():
    lina.deiconify()

#Ventana Menu
menu = Tk()
menu.title("Pinball Game")
menu.resizable(0,0)
menu.geometry("300x400")
canvas2 = Canvas(menu,width=300, height = 400)
canvas2.pack(fill="none")
empezar = Button(menu, text = "Play", font = "Algerian", command=mostrar).place(x=20, y=60)
cargar = Button(menu, text = "Loaded Game", font = "Algerian", command = mostrar).place(x=20,y=140)
manual = Button(menu, text = "Manual", font = "Algerian", command = mostrar).place(x=20,y=180)
nombre = Button(menu, text = "Player Name:", font = "Algerian", command = mostrar).place(x = 20, y=100)
fondo = PhotoImage(file = "dri.gif")
canvas2.create_image(0,0, image = fondo)
salir = Button(menu, text = "End Game", font = "Algerian", command = exit).place(x=20,y=220)
title = PhotoImage(file = "ab.gif")
canvas2.create_image(200,330, image = title)



#Ventana del juego
lina = Toplevel(menu)
c = Canvas(lina,width=400, height = 800)
c.pack()
c.config(bg="LightSteelBlue2")
lina.title("Pinball Game")
player = Label(c,text="Name:", fg = "blue", font = "Algerian")
techo = {"objeto":c.create_polygon(20,0,20,20,380,20,380,0, fill = "tomato")}
esquina1 = {"objeto":c.create_polygon(50,0,0,70,0,0, fill = "red")}
esquina2 = {"objeto":c.create_polygon(350,0,400,70,400,0, fill = "red")}
c.create_line(365,600,365,110, fill = "green")
ob1 = {"objeto":c.create_polygon(30,570,100,570,100,550,30,530, fill = "orange")}
c.create_polygon(100,570,170,570,100,550, fill = "yellow")
ob2 = {"objeto":c.create_polygon(365,570,295,570,295,550,365,530, fill = "orange")}


ball = {"dx": 0, "dy":-10, "objeto":c.create_oval(370, 570, 400, 600, fill= "black")}


bolita1 = {"objeto":c.create_rectangle(65,90,115,130, fill = "blue")}

bolita3 = {"objeto":c.create_rectangle(260,90,310,130, fill = "blue")}
triangulo1 = {"objeto":c.create_rectangle(60,490,110,440, fill = "lawn green")}
triangulo2 = {"objeto":c.create_rectangle(320,490,270,440, fill = "lime green")}

palanca_1 = c.create_polygon(100,570,180,570,100,550, fill = "yellow")
palanca_2 = c.create_polygon(295,570,215,570,295,550, fill = "yellow")
center = {"objeto":c.create_rectangle(165,320,205,350, fill = "DarkOrchid3")}
          

    
def moveball1(event):
    moveBall()


def moveBall():
    x1, y1, x2, y2 = c.coords(ball["objeto"])
    
    x = (x1+x2)//2
    y = (y1+y2)//2
    dx = 4
    
    if x<15 or x>385:
        ball["dx"] *= -1
    if y<15 or y>585:
        ball["dy"] *= -1

    pelota = c.find_overlapping(x1,y1,x2,y2)
    print (pelota)

    if pelota == (8,13):
        ball["dx"] *= 1
        ball["dy"] *= -1
    if pelota == (8,14):
        ball["dx"] *= 1
        ball["dy"]*=-1
    if pelota == (5,8):
        ball["dx"] *= -1
        ball["dy"]*=1
    if pelota == (1,8):
        ball["dx"] *= 1
        ball["dy"]*=-1
    if pelota == (8,11):
        ball["dx"] == 1
        ball["dy"] == -1
    if pelota == (6,8,16):
        ball["dx"] *= 1
        ball["dy"] *= -1
    if pelota == (8,16):
        ball["dx"] *= 1
        ball["dy"]*=-1
    if pelota == (4,8,15):
        ball["dx"] *= 1
        ball["dy"]*=-1
    if pelota == (8,17):
        ball["dx"] *= 1
        ball["dy"]*=-1
    if pelota == (7,8,17):
        ball["dx"] *= -1
        ball["dy"]*=1
    if pelota == (8,12):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (8,10):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (8,18):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (5,10,15):
        ball["dx"] = random.randint(-8, -5)
        ball["dy"] = random.randint(0, 1)
    if pelota == (3, 8):
        ball["dx"] = random.randint(-8, -5)
        ball["dy"] = random.randint(0, 1)
    if pelota == (7,15):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (8,15):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (4,7,8):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (4,8):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (1,2,8):
        ball["dx"] == -1
        ball["dy"] == 1
    if pelota == (5,15):
        ball["dx"] == -1
        ball["dy"] == 1
    if pelota == (1,3,8):
        ball["dx"] *= -1
        ball["dy"] *= -1
    if pelota == (6,8,13):
        ball["dx"] *= -1
        ball["dy"] *= -1
    if pelota == (8,9):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (8,95):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (7,8,95):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (7,8,97):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (7,8,91):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (8,93):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (7,8,27):
        ball["dx"] *= -1
        ball["dy"] *= 1
    if pelota == (5,6,8,31):
        ball["dx"] *= -1
        ball["dy"] *= 1
    c.move(ball["objeto"], ball["dx"], ball["dy"])
    lina.after(20, moveBall)
    ball["dy"] += 0.04



#movimiento paletas
def pal1(event):    
    global palanca_1
        
    c.delete(palanca_1)
    palanca_1 = c.create_polygon(130,560,180,530,100,550, fill = "yellow")
    c.update()
    c.delete(palanca_1)
    time.sleep(0.05)
    palanca_1 = c.create_polygon(100,570,180,570,100,550, fill = "yellow")
    
lina.bind('c',pal1)


def pal2(event):
    global palanca_2
        
    c.delete(palanca_2)        
    palanca_2 = c.create_polygon(265,560,215,530,295,550, fill = "yellow")
    c.update()
    c.delete(palanca_2)
    time.sleep(0.07)
    palanca_2 = c.create_polygon(295,570,215,570,295,550, fill = "yellow")
  
lina.bind('m',pal2)



lina.bind('<space>',moveball1)

lina.withdraw()
menu.mainloop()
