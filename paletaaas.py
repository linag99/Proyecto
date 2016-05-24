#Palanca Izquierda
xy = [(600,703), (600,718), (680,711), (680,704)]
palanca_izquierda = canvas.create_polygon(xy,fill="black",outline="white", width=2)

new_xy = [(600,703), (600,718), (680,676), (680,669)]

#Palanca Derecha
xs = [(800,703), (800,718), (720,711), (720,704)] 
palanca_derecha = canvas.create_polygon(xs,fill="black",outline="white",width=2)

new_xs = [(800,703), (800,718), (720,676), (720,669)]


def start_game(event):
    start_game1()


def mover_palanca_izquierda(event):

    global xy, palanca_izquierda, new_xy
    
    canvas.delete(palanca_izquierda)
    palanca_izquierda = canvas.create_polygon(new_xy,fill="black",outline="white")
    canvas.update()
    canvas.delete(palanca_izquierda)
    palanca_izquierda = canvas.create_polygon(xy,fill="black",outline="white")
    time.sleep(0.05)


def mover_palanca_derecha(event):
    
    global xs, palanca_derecha, new_xs
    
    canvas.delete(palanca_derecha)
    palanca_derecha = canvas.create_polygon(new_xs,fill="black",outline="white")
    canvas.update()
    canvas.delete(palanca_derecha)
    palanca_derecha = canvas.create_polygon(xs,fill="black",outline="white")
    time.sleep(0.05)
    
    
v1.bind("<Left>", mover_palanca_izquierda)
v1.bind("<Right>", mover_palanca_derecha)
v1.bind('z', start_game)

