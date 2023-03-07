#Flores Romero Andres Gael
#07/023/2023

from tkinter import *
from tkinter import ttk
import tkinter as tk

class Inicio:

    def __init__(self, root):

        root.title("Inicio de Sesión")
        
        self.usuario = StringVar()
        self.contraseña = StringVar()

        mainFrame = ttk.Frame(root)
        mainFrame.grid(column= 1, row= 0)

        #Entrys
        usuarioEntry = ttk.Entry(mainFrame,textvariable=self.usuario, width=30)
        usuarioEntry.grid(column=1, row=1)
        contraseñaEntry = ttk.Entry(mainFrame,textvariable=self.contraseña, width=30)
        contraseñaEntry.grid(column=1,row=3)

        #Buttons
        ttk.Button(mainFrame, text = "Ingresar").grid(column= 1, row = 5, sticky=(E))

        #Labels
        ttk.Label(mainFrame, text= " ").grid(column=0, row=0)
        ttk.Label(mainFrame, text= " ").grid(column=0, row=1)
        ttk.Label(mainFrame, text= " ").grid(column=1, row=2)
        ttk.Label(mainFrame, text= " ").grid(column=1, row=4)
        ttk.Label(mainFrame, text= "Usuario: ").grid(column=0,row=1)
        ttk.Label(mainFrame, text= " ").grid(column=0, row=2)
        ttk.Label(mainFrame, text= "Contraseña: ").grid(column=0,row=3)

