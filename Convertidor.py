#App para convertir pies a metros por medio de Tkinter
#Flores Romero Andres Gael
#23/02/2023

#Importacion para Tkinter
from tkinter import *
from tkinter import ttk

class Convertidor: 

    #Contructor de la clase
    def __init__(self, root):
        
        root.title("Pies a metros")
        
        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(root)
        mainFrame.grid(column= 1, row= 0)

        piesEntry = ttk.Entry(mainFrame, textvariable= self.pies)
        piesEntry.grid(column= 1, row=0)
        ttk.Label(mainFrame, text= "Pies").grid(column= 2, row= 0)
        ttk.Label(mainFrame, text= "Son equivalentes a: ").grid(column= 0, row= 1)
        ttk.Label(mainFrame, textvariable= self.metros).grid(column= 1, row= 1)
        ttk.Label(mainFrame, text= "Metros").grid(column= 2, row= 1)
        ttk.Button(mainFrame, text = "Convertir", command= self.Calcular).grid(column= 2, row = 2)
        
        #Hacer la operacion presionando ENTER

        root.bind("<Return>", self.Calcular)

    def Calcular(self, *args):
        try:
            piesIngresados = float(self.pies.get()) #Siempre devuelve una cadena
            metros = piesIngresados / 3.2808
            print("Metros: ", metros )
            self.metros.set(metros)
        except ValueError:
            print("Valor no admitido...Intente de nuevo.")

        print("Pies ingresado: ", self.pies.get())






    


    
    




