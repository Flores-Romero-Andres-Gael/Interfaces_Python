from tkinter import *
from tkinter import ttk

root = Tk
etqTexto = ttk.Label(root, text="Etiqueta de solo texto")
etqTexto.grid()

imagen = PhotoImage(file="https://www.google.com/url?sa=i&url=https%3A%2F%2Fopenwebinars.net%2Fblog%2Fpython-principales-caracteristicas%2F&psig=AOvVaw1GdX8pHW9ragIAb3DgMVe8&ust=1678323903346000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKjxv_KRy_0CFQAAAAAdAAAAABAP")

etqImagen = ttk.Label(root)
etqImagen.grid()
