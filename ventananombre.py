from tkinter import*
jugador = Tk()
cuadro1 = Label(jugador, text = "Nombre del jugador:")
cuadro1.grid(row = 1, column = 1)
variable = StringVar()
ventana = Entry(jugador,textvariable = variable)
ventana.grid(row = 1, column = 2)
jugador.mainloop()
