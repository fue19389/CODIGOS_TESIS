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

class pGUI:


    def __init__(self):

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración Inicial ----------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        # Se crea la interfaz general
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

        # Inicialización de librerías personales
        self.feed = fD.ModelFeeder()
        self.ppr = eD.GetModelData()
        self.train = mG.ModelGenerate()
        self.use_m = lT.UseModel()

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Captura de fotografías -----------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.label1 = ctk.CTkLabel(self.tabview.tab('Captura de fotografías'), \
                                   text='1. Escoja la posición de la cabeza\n 2. Presione el botón\n 3. Presione: Enter ', \
                                   font=('aptos', 26))
        self.label1.pack(padx=20, pady=45)
        self.buttonFrame = ctk.CTkFrame(self.tabview.tab('Captura de fotografías'))

        self.btn1 = ctk.CTkButton(self.buttonFrame, text='IZQ-UP', font=('aptos', 18), width=250, height=75, command=self.actL0)
        self.btn1.grid(row=0, column=0, padx=10, pady=10)

        self.btn2 = ctk.CTkButton(self.buttonFrame, text='UP', font=('aptos', 18), width=250, height=75, command=self.actL3)
        self.btn2.grid(row=0, column=1, padx=10, pady=10)

        self.btn3 = ctk.CTkButton(self.buttonFrame, text='DER-UP', font=('aptos', 18), width=250, height=75, command=self.actL2)
        self.btn3.grid(row=0, column=2, padx=10, pady=10)

        self.btn4 = ctk.CTkButton(self.buttonFrame, text='IZQ', font=('aptos', 18), width=250, height=75, command=self.actL0)
        self.btn4.grid(row=1, column=0, padx=10, pady=10)

        self.btn5 = ctk.CTkButton(self.buttonFrame, text='FRONT', font=('aptos', 18), width=250, height=75, command=self.actL1)
        self.btn5.grid(row=1, column=1, padx=10, pady=10)

        self.btn6 = ctk.CTkButton(self.buttonFrame, text='DER', font=('aptos', 18), width=250, height=75, command=self.actL2)
        self.btn6.grid(row=1, column=2, padx=10, pady=10)

        self.btn7 = ctk.CTkButton(self.buttonFrame, text='IZQ-DOWN', font=('aptos', 18), width=250, height=75, command=self.actL0)
        self.btn7.grid(row=2, column=0, padx=10, pady=10)

        self.btn8 = ctk.CTkButton(self.buttonFrame, text='DOWN', font=('aptos', 18), width=250, height=75, command=self.actL1)
        self.btn8.grid(row=2, column=1, padx=10, pady=10)

        self.btn9 = ctk.CTkButton(self.buttonFrame, text='DER-DOWN', font=('aptos', 18), width=250, height=75, command=self.actL2)
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

        self.btn_load = ctk.CTkButton(self.buttonFrame2, text='Cargar Serie', font=('aptos', 18), width=250, height=75, command=self.load)
        self.btn_load.grid(row=0, column=0, padx=10, pady=10)

        self.btn_prepare = ctk.CTkButton(self.buttonFrame2, text='Preparar Serie', font=('aptos', 18), width=250, height=75, command=self.prepare)
        self.btn_prepare.grid(row=0, column=1, padx=10, pady=10)

        self.btn_erase = ctk.CTkButton(self.buttonFrame2, text='Borrar Serie', font=('aptos', 18), width=250, height=75, command=self.erase)
        self.btn_erase.grid(row=1, column=0, padx=10, pady=10)

        self.btn_reset = ctk.CTkButton(self.buttonFrame2, text='Resetear Modelo', font=('aptos', 18), width=250, height=75, command=self.reset)
        self.btn_reset.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame2.pack(pady=20)

        self.btn_train = ctk.CTkButton(self.tabview.tab('Manejo de datos'), text='Entrenar modelo', font=('aptos', 18), width=250, height=75, command=self.trainM)
        self.btn_train.pack(padx=10, pady=10)
        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Prueba en vivo -------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.btn_run = ctk.CTkButton(self.tabview.tab('Prueba en vivo'), text='Ejecutar', font=('aptos', 30),
                                       width=350, height=150, command=self.turnon)
        self.btn_run.pack(padx=50, pady=(50, 0))

        self.btn_stop = ctk.CTkButton(self.tabview.tab('Prueba en vivo'), text='Detener', font=('aptos', 30),
                                       width=350, height=150, command=self.turnoff)
        self.btn_stop.pack(padx=50, pady=(50, 0))

        self.label3 = ctk.CTkLabel(self.tabview.tab('Prueba en vivo'), text='Para terminar presione: Esc', font=('aptos', 22))
        self.label3.pack(pady=20, padx=20)

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración final  -----------------------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funciones de botones para fotos ------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------
    def actL0(self):
        self.feed.takePHOTO(0)

    def actL1(self):
        self.feed.takePHOTO(1)

    def actL2(self):
        self.feed.takePHOTO(2)

    def actL3(self):
        self.feed.takePHOTO(3)

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funciones para manejo de datos  ------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def prepare(self):
        if self.optionmenu_1.get() == 'Entrenamiento':
            self.ppr.prepareD(0)
        elif self.optionmenu_1.get() == 'Validación':
            self.ppr.prepareD(1)
        messagebox.showinfo(message='Listo')
    def load(self):
        if self.optionmenu_1.get() == 'Entrenamiento':
            self.feed.loadD(0)
        elif self.optionmenu_1.get() == 'Validación':
            self.feed.loadD(1)
        messagebox.showinfo(message='Listo')
    def reset(self):
        if self.optionmenu_1.get() == 'Entrenamiento':
            self.feed.resetMaster(0)
        elif self.optionmenu_1.get() == 'Validación':
            self.feed.resetMaster(1)
        messagebox.showinfo(message='Listo')
    def erase(self):
        self.feed.eraseSERIES()
        messagebox.showinfo(message='Listo')
    def trainM(self):
        self.train.TrainModel()
        messagebox.showinfo(message='Listo')

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funcion para prueba en vivo  ---------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def turnon(self):
        self.use_m.on()

    def turnoff(self):
        self.use_m.stop()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funcion de cerrardo  -----------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def on_closing(self):
        self.feed.eraseSERIES()
        self.root.destroy()


pGUI()
