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
import photoMODEL as pM
import graphMODEL as gM
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
        self.tabview.add('Instrucciones Captura')
        self.tabview.add("Captura de fotografías")
        self.tabview.add("Manejo de datos")
        self.tabview.add('Prueba en vivo')
        self.tabview.pack()

        # Inicialización de librerías personales
        self.feed = fD.ModelFeeder()
        self.ppr = eD.GetModelData()
        self.train = pM.ModelPhoto()
        self.train1 = gM.ModelGraph()
        self.use_m = lT.UseModel()

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Instrucciones -----------------------------------
        # --------------------------------------------------------------------------------------------------------------
        self.label0 = ctk.CTkLabel(self.tabview.tab('Instrucciones Captura'),
                                   text='1. Primeros 3 sonidos de preparación \n 2. Al finalizar otro sonido alertará', font=('aptos', 26))
        self.label0.pack(padx=20, pady=45)
        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Captura de fotografías -----------------------------------
        # --------------------------------------------------------------------------------------------------------------


        self.btn1 = ctk.CTkButton(self.tabview.tab('Captura de fotografías'), text='CAPTURAR', font=('aptos', 30),
                                  width=350, height=150, command=self.actL)
        self.btn1.pack(padx=50, pady=50)

        self.label1 = ctk.CTkLabel(self.tabview.tab('Captura de fotografías'),
                                   text='Movimientos: \n 1.Izquierda (UP-DOWN) \n 2. Centro-Abajo \n 3. Derecha (UP-DOWN) \n 4. Arriba (DER-IZQ, CORTOS)', font=('aptos', 20))
        self.label1.pack(padx=20, pady=45)

        # --------------------------------------------------------------------------------------------------------------
        # ----------------------------- Configuración de Tab: Manejo de datos ------------------------------------------
        # --------------------------------------------------------------------------------------------------------------

        self.label2 = ctk.CTkLabel(self.tabview.tab('Manejo de datos'), text='Escoja tipo de datos:', font=('aptos', 22))
        self.label2.pack(padx=15, pady=(20,0))

        self.buttonFrame2 = ctk.CTkFrame(self.tabview.tab('Manejo de datos'))

        self.btn_erase = ctk.CTkButton(self.buttonFrame2, text='Borrar Serie', font=('aptos', 18), width=250, height=75, command=self.erase)
        self.btn_erase.grid(row=0, column=0, padx=10, pady=10)

        self.btn_reset = ctk.CTkButton(self.buttonFrame2, text='Resetear Modelo', font=('aptos', 18), width=250, height=75, command=self.reset)
        self.btn_reset.grid(row=0, column=1, padx=10, pady=10)

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
    def actL(self):
        self.feed.takePHOTO()

    # --------------------------------------------------------------------------------------------------------------
    # ----------------------------- Funciones para manejo de datos  ------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------

    def reset(self):
        self.feed.resetMaster()
        messagebox.showinfo(message='Listo')
    def erase(self):
        self.feed.eraseSERIES()
        messagebox.showinfo(message='Listo')
    def trainM(self):
        self.feed.loadD()
        self.feed.eraseSERIES()
        self.train1.TrainModel()
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
