# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código prueba para la GUI que involucra todos los otros códigos

# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

# Librerías para funciones
import os
import cv2
import numpy as np
import pandas as pd
import seaborn as sn
import tensorflow as tf
from matplotlib import pyplot as plt
from matplotlib import rcParams

import feedDATA as fD
import extractDATA as eD
import modelGENERATOR as mG
import liveTEST as lT

# Librerías para GUI
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


# ------------------------------------------------
# ----- Interfaz ---------------------------------
# ------------------------------------------------

class ProjectGUI:

    def __init__(self):
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
        self.root = ctk.CTk()

        self.root.geometry('1000x625')
        self.root.title('HO GUI')

        # Se crea la selección de pestañas
        self.tabview = ctk.CTkTabview(self.root, width=900, height=575)
        self.tabview.add("Captura de fotografías")
        self.tabview.add("Manejo de datos")
        self.tabview.add('Prueba en vivo')
        self.tabview.pack()

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Captura de fotografías -----------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.label1 = ctk.CTkLabel(self.tabview.tab('Captura de fotografías'), \
                                   text='1. Posicione su cabeza según la dirección del botón\n 2. Presione el botón\n 3. Presione Enter para capturar ', \
                                   font=('aptos', 26))
        self.label1.pack(padx=20, pady=45)
        self.buttonFrame = ctk.CTkFrame(self.tabview.tab('Captura de fotografías'))

        self.btn1 = ctk.CTkButton(self.buttonFrame, text='IZQ-UP', font=('aptos', 18), width=250, height=75)
        self.btn1.grid(row=0, column=0, padx=10, pady=10)

        self.btn2 = ctk.CTkButton(self.buttonFrame, text='UP', font=('aptos', 18), width=250, height=75)
        self.btn2.grid(row=0, column=1, padx=10, pady=10)

        self.btn3 = ctk.CTkButton(self.buttonFrame, text='DER-UP', font=('aptos', 18), width=250, height=75)
        self.btn3.grid(row=0, column=2, padx=10, pady=10)

        self.btn4 = ctk.CTkButton(self.buttonFrame, text='IZQ', font=('aptos', 18), width=250, height=75)
        self.btn4.grid(row=1, column=0, padx=10, pady=10)

        self.btn5 = ctk.CTkButton(self.buttonFrame, text='FRONT', font=('aptos', 18), width=250, height=75)
        self.btn5.grid(row=1, column=1, padx=10, pady=10)

        self.btn6 = ctk.CTkButton(self.buttonFrame, text='DER', font=('aptos', 18), width=250, height=75)
        self.btn6.grid(row=1, column=2, padx=10, pady=10)

        self.btn7 = ctk.CTkButton(self.buttonFrame, text='IZQ-DOWN', font=('aptos', 18), width=250, height=75)
        self.btn7.grid(row=2, column=0, padx=10, pady=10)

        self.btn8 = ctk.CTkButton(self.buttonFrame, text='DOWN', font=('aptos', 18), width=250, height=75)
        self.btn8.grid(row=2, column=1, padx=10, pady=10)

        self.btn9 = ctk.CTkButton(self.buttonFrame, text='DER-DOWN', font=('aptos', 18), width=250, height=75)
        self.btn9.grid(row=2, column=2, padx=10, pady=10)

        self.buttonFrame.pack()

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Manejo de datos ------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.label2 = ctk.CTkLabel(self.tabview.tab('Manejo de datos'), text='Escoja tipo de datos:', font=('aptos', 22))
        self.label2.pack(padx=15, pady=(20,0))
        self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab('Manejo de datos'), dynamic_resizing=False,
                                                        values=["Entrenamiento", "Validación"], width=200, height=40, font=('aptos', 18))
        self.optionmenu_1.pack(padx=20, pady=20)
        self.buttonFrame2 = ctk.CTkFrame(self.tabview.tab('Manejo de datos'))

        self.btn_prepare = ctk.CTkButton(self.buttonFrame2, text='Preparar', font=('aptos', 18), width=250, height=75)
        self.btn_prepare.grid(row=0, column=0, padx=10, pady=10)

        self.btn_load = ctk.CTkButton(self.buttonFrame2, text='Cargar', font=('aptos', 18), width=250, height=75)
        self.btn_load.grid(row=0, column=1, padx=10, pady=10)

        self.btn_erase = ctk.CTkButton(self.buttonFrame2, text='Borrar', font=('aptos', 18), width=250, height=75)
        self.btn_erase.grid(row=1, column=0, padx=10, pady=10)

        self.btn_reset = ctk.CTkButton(self.buttonFrame2, text='Resetear', font=('aptos', 18), width=250, height=75)
        self.btn_reset.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame2.pack(pady=20)

        self.btn_train = ctk.CTkButton(self.tabview.tab('Manejo de datos'), text='Entrenar modelo', font=('aptos', 18), width=250, height=75)
        self.btn_train.pack(padx=10, pady=10)
        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Prueba en vivo -----------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.btn_train = ctk.CTkButton(self.tabview.tab('Prueba en vivo'), text='Ejecutar', font=('aptos', 30),
                                       width=350, height=150)
        self.btn_train.pack(padx=50, pady=(175, 0))
        self.root.mainloop()


ProjectGUI()
