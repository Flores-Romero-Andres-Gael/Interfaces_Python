#Flores Romero Andres Gael
#09/03/2023

#Importacion para Tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

#---------------------------------PADRE--------------------------------------
root = Tk()
root.title("Muestra Widgets")

#---------------------------------FRAMES--------------------------------------

#Primero
mainFrame = ttk.Frame(root, padding= "20 20 20 20")
mainFrame.grid(column=0, row=0)

#Segundo
mainFrame2 = ttk.Frame(mainFrame, relief="raised",padding= "10 10 10 10", width= 20, height= 20)
mainFrame2.grid(column=0, row=1, sticky=(W))
#Tercero
mainFrame3 = ttk.Frame(mainFrame,relief="raised",padding= "10 10 10 10",width= 20, height= 20)
mainFrame3.grid(column=0, row=2, sticky=(W), pady=5)
#Cuarto
mainFrame4 = ttk.Frame(mainFrame,padding= "10 10 10 10")
mainFrame4.grid(column=1, row=1, sticky=(W), pady=5)
#-----------------------------------DATOS-------------------------------------
#PrimerFrame
Estados = StringVar()
#SegundoFrame
nombreVar = StringVar()
APaternoVar = StringVar()
AMaternoVar = StringVar()
CorreoVar = StringVar()
NumeroMovilVar = IntVar()

#----------------------------------ENTRYS-------------------------------------
#SegundoFrame
NombreEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=0,pady=5)
APaternoEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=1,pady=5)
AMaternoEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=2,pady=5)
CorreoEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=3,pady=5)
NumeroEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=4,pady=5)

#----------------------------------LABELS------------------------------------

#Primer Frame

#Segundo Frame
ttk.Label(mainFrame2, text= "Nombre: ").grid(column=0, row=0, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "A. Paterno: ").grid(column=0, row=1, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "A. Materno: ").grid(column=0, row=2, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "Correo: ").grid(column=0, row=3, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "Movil: ").grid(column=0, row=4, pady= 5, sticky=(E))

#TercerFrame
ttk.Label(mainFrame3, text= "Aficiones: ").grid(column=0, row=0, sticky=(W))

#----------------------------------BOTTONS-------------------------------------
#Primer Frame
ttk.Button(mainFrame, text="Guardar").grid(column=0, row=3, sticky=(W))
ttk.Button(mainFrame, text="Cancelar").grid(column=0, row=3, padx= 120 ,sticky=(W))

combosEstados = ttk.Combobox(mainFrame, textvariable=Estados)
combosEstados.grid(column=1, row=2)
combosEstados['values'] = ("Aguascalientes",
                            "Baja California","Baja California Sur", "Campeche","Coahuila",
                            "Colima","Chiapas","Chihuahua","Durango","Distrito Federal","Guanajuato",
                            "Guerrero","Hidalgo","Jalisco","México","Michoacán","Morelos", "Nayarit", 
                            "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", 
                            "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", 
                            "Zacatecas")


#Tercer Frame
ttk.Checkbutton(mainFrame3, text="Leer").grid(column=0,row=1,pady=5, sticky=(W))
ttk.Checkbutton(mainFrame3, text="Musica").grid(column=1,row=1,pady=5, padx=5, sticky=(W))
ttk.Checkbutton(mainFrame3, text="Videojuegos").grid(column=2,row=1,pady=5, padx=5, sticky=(W))

#Cuarto Frame
ttk.Radiobutton(mainFrame4, text="Estudiante").grid(column=0, row=0, padx=20, sticky=(W)) 
ttk.Radiobutton(mainFrame4, text="Empleado").grid(column=0 , row=1, padx=20, sticky=(W)) 
ttk.Radiobutton(mainFrame4, text="Desempleado").grid(column=0, row=2, padx=20, sticky=(W)) 


root.mainloop()

