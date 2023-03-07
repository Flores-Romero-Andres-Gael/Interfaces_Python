#App para convertir pies a metros por medio de Tkinter
#Flores Romero Andres Gael
#23/02/2023

#Importacion para Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Convertidor: 

    #Contructor de la clase
    def __init__(self, root):
        
        root.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(root, padding="12 12 12 30")
        #Izquierda, arriba, derecha, abajo
        mainFrame.grid(column= 1, row= 0, sticky= (W, E))

        piesEntry = ttk.Entry(mainFrame, width= 15, textvariable= self.pies)
        piesEntry.grid(column= 1, row=0)
        ttk.Label(mainFrame, text= "Pies").grid(column= 2, row= 0, sticky=(W))
        ttk.Label(mainFrame, text= "Son equivalentes a: ").grid(column= 0, row= 1, sticky=(W))
        ttk.Label(mainFrame, textvariable= self.metros).grid(column= 1, row= 1)
        ttk.Label(mainFrame, text= "Metros").grid(column= 2, row= 1,sticky=(W))
        ttk.Button(mainFrame, text = "Convertir", command= self.Calcular).grid(column= 2, row = 2)
        
        piesEntry.focus()
        #Hacer la operacion presionando ENTER
        root.bind("<Return>", self.Calcular)

    def Calcular(self, *args):
        try:
            piesIngresados = float(self.pies.get()) #Siempre devuelve una cadena
            metros = piesIngresados / 3.2808
            print("Metros: ", metros )
            self.metros.set(metros)
            self.pies.set("")
            ttk.Label(text= " ").grid(column= 1, row= 2,sticky=(S))
        except ValueError:
            print("Valor no admitido...Intente de nuevo.")
            messagebox.showinfo("ERROR", "Este dato no es valido.")
            self.pies.set("")

        print("Pies ingresado: ", self.pies.get())






    


    
    




