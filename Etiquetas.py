from tkinter import *
from tkinter import ttk


root = Tk()
etqTexto = ttk.Label(root, text= "Etiqueta de solo texto")
etqTexto.grid()

imagen = PhotoImage(file = 'python.png')

etqImagen = ttk.Label(root)
etqImagen.grid()
etqImagen ['image'] = imagen

etqCombinada = ttk.Label(root, text="etqCombinada", compound="center")
etqCombinada.grid()
etqCombinada ['image'] = imagen

root.mainloop()