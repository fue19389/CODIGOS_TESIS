# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código para realizar pruebas de reconocimiento de orientación de cabeza

# ------------------------------------------------------
# -----------------Librerías a utilizar-----------------
# ------------------------------------------------------

import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt

class UseModel:

    def __init__(self):
        # ------------------------------------------------------
        # -----------------Selección de modelo------------------
        # ------------------------------------------------------
        
        # Actualmente, se tienen modelos del 0 -> 6
        self.n_model = 4
        # -----------------------------------------------------

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------
        
        # Directorio para guardar las variables a exportar
        self.expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'

    # -----------------------------------------------------
    # -------------------Cargar modelo---------------------
    # -----------------------------------------------------

        if self.n_model == 0:
            self.mname = 'head_or.keras'
        elif self.n_model == 1:
            self.mname = 'head_or1.keras'
        elif self.n_model == 2:
            self.mname = 'head_or2.keras'
        elif self.n_model == 3:
            self.mname = 'head_or3.keras'
        elif self.n_model == 4:
            self.mname = 'head_or4.keras'
        elif self.n_model == 5:
            self.mname = 'head_or5.keras'
        elif self.n_model == 6:
            self.mname = 'head_or6.keras'

        self.ho_model = os.path.join(self.expordir, self.mname)
        self.ho_model = tf.keras.models.load_model(self.ho_model)

         
    def start(self):

        # -----------------------------------------------------
        # ---------Inicialización de la Webcam---- ------------
        # -----------------------------------------------------

        cap = cv2.VideoCapture(0)
        
        # -----------------------------------------------------
        # ----Visualizar el predict del modelo LIVE------------
        # -----------------------------------------------------
        
        while True:
        
            # Saving captured image and transforming from BGR TO RGB
        
            _, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = cv2.resize(imgRGB, (320, 180))
            imgRGB = imgRGB.astype(int)/255
        
            y_predicted = self.ho_model.predict(np.array([imgRGB]), verbose=None)
            prediction = np.argmax(y_predicted)
            print(prediction)
        
            # Show the complete image
            cv2.imshow('Image', img)
        
            key = cv2.waitKey(30)
            if key == 27: # 13 = enter, 27 = esc
                break