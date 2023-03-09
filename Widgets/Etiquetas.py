from tkinter import *
from tkinter import ttk


root = Tk()
etqTexto = ttk.Label(root, text= "Ana de armas", font="arial", foreground= "blue")
etqTexto.grid()

imagen = PhotoImage(file = 'AnadeAr.png')

etqImagen = ttk.Label(root)
etqImagen.grid()
etqImagen ['image'] = imagen

#"compound = compuesta "
etqCombinada = ttk.Label(root, text="My girlfriend", foreground= "blue", font= ("arial", 20), background = "blue", compound="center")
etqCombinada.grid()
etqCombinada ['image'] = imagen

root.mainloop()