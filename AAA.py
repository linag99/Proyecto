from tkinter import*

lina = Tk()
c = Canvas(lina,width=400, height = 600)
c.pack()

ob1 = {"objeto":c.create_polygon(50,0,0,70,0,0, fill = "red")}
ob2 = {"objeto":c.create_polygon(370,0,400,70,400,0, fill = "red")}
c.create_line(365,600,365,80, fill = "green")
ob3 = {"objeto":c.create_polygon(30,570,100,570,100,550,30,530, fill = "orange")}
palanca = {"objeto":c.create_polygon(100,570,170,570,100,550, fill = "yellow")}
ob5 = {"objeto":c.create_polygon(365,570,295,570,295,550,365,530, fill = "orange")}
palanca2 = {"objeto":c.create_polygon(295,570,225,570,295,550, fill = "yellow")}
ball = {"dx": 0, "dy":-5, "objeto":c.create_oval(370, 570, 400, 600, fill= "black")}
ob6 = {"objeto":c.create_polygon(20,0,20,20,380,20,380,0, fill = "red")}
ob7 = {"objeto":c.create_oval(65,100,115,130, fill = "blue")}
ob8 = {"objeto":c.create_oval(160,130,200,180, fill = "cyan")}
ob9 = {"objeto":c.create_oval(260,100,310,130, fill = "blue")}

def palancaUp(t):
    palanca["objeto"]= c.create_polygon(100,550,120,560,190,540, fill = "yellow")
lina.bind("c", palancaUp)


def moveBall():
    x1, y1, x2, y2 = c.coords(ball["objeto"])
    x = (x1+x2)//2
    y = (y1+y2)//2
    dx = 4
    if x<15 or x>385:
        ball["dx"]*=-1
    if y<15 or y>585:
        ball["dy"]*=-1
    c.move(ball["objeto"], ball["dx"], ball["dy"])
    lina.after(1, moveBall)

lina.after(1, moveBall)

