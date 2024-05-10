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
import threading
import numpy as np
import turtle as ttl
import tensorflow as tf
import faceLANDMARKS as fL
import mediapipe as mp
from tensorflow import keras
from tensorflow.keras.optimizers import SGD
import matplotlib.pyplot as plt

# Actualmente, se tienen modelos del 0 -> 8
n_model = 12

# -----------------------------------------------------

# ------------------------------------------------
# ----- Directorios a utilizar -------------------
# ------------------------------------------------

# Directorio para guardar las variables a exportar
expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'

# detector de landmarks
detector = fL.FaceMeshDetector()
# predicción incial
prediction = 1
predictionM = 1

if  n_model in range(13):
     mname = f'head_or{ n_model}.keras'
     mnameM = f'head_or{ n_model}M.keras'
     ho_model = os.path.join( expordir,  mname)
     ho_model = tf.keras.models.load_model( ho_model)
     mo_model = os.path.join( expordir,  mnameM)
     mo_model = tf.keras.models.load_model( mo_model)
else:
    raise ValueError("Invalid model number")

cap = cv2.VideoCapture(0)


while True:
    _, img = cap.read()
    img, nodes =  detector.findMouthMesh(img)
    nodes = np.array([nodes])
    # Check if any face landmarks were detected
    if nodes.any() != 0:
        y_predicted = mo_model.predict(nodes, verbose=0)
        predictionM = int(np.argmax(y_predicted))
    else:
        predictionM = 0
    print(predictionM)

