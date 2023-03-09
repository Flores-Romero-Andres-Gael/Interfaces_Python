from tkinter import *
from tkinter import ttk

root = Tk()

estado = StringVar()

comboEstados = ttk.Combobox(root, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

root.mainloop()