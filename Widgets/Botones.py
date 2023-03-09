from tkinter import *
from tkinter import ttk

root = Tk()
boton = ttk.Button(root, text= "Boton solo texto")
boton.grid()

imagen = PhotoImage(file = "Dua.png")

btnImagen = ttk.Button(root)
btnImagen.grid()
btnImagen ['image'] = imagen

botonCombinada = ttk.Label(root, text="BotonCombinada", compound="center")
botonCombinada.grid()
botonCombinada ['image'] = imagen

chkBoton = ttk.Checkbutton(root, text= "Opcion 1")
chkBoton.grid()


root.mainloop()