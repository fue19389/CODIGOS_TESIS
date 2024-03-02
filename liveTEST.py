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

# ------------------------------------------------------
# -----------------Selección de modelo------------------
# ------------------------------------------------------

# Actualmente, se tienen modelos del 0 -> 6
n_model = 4
# -----------------------------------------------------

# ------------------------------------------------
# ----- Directorios a utilizar -------------------
# ------------------------------------------------

# Directorio para guardar las variables a exportar
expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'

# -----------------------------------------------------
# -------------------Cargar modelo---------------------
# -----------------------------------------------------

if n_model == 0:
    mname = 'head_or.keras'
elif n_model == 1:
    mname = 'head_or1.keras'
elif n_model == 2:
    mname = 'head_or2.keras'
elif n_model == 3:
    mname = 'head_or3.keras'
elif n_model == 4:
    mname = 'head_or4.keras'
elif n_model == 5:
    mname = 'head_or5.keras'
elif n_model == 6:
    mname = 'head_or6.keras'

ho_model = os.path.join(expordir, mname)
ho_model = tf.keras.models.load_model(ho_model)

# -----------------------------------------------------

# -----------------------------------------------------
# ---------Inicialización de la Webcam---- ------------
# -----------------------------------------------------

# # Capture webcam
#
cap = cv2.VideoCapture(0)

# Capture webcam & Set resolution

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

# ----------------------------------------------------

# -----------------------------------------------------
# ----Visualizar el predict del modelo LIVE------------
# -----------------------------------------------------

while True:

    # Saving captured image and transforming from BGR TO RGB

    _, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = cv2.resize(imgRGB, (320, 180))
    imgRGB = imgRGB.astype(int)/255

    y_predicted = ho_model.predict(np.array([imgRGB]), verbose=None)
    prediction = np.argmax(y_predicted)
    print(prediction)

    # Show the complete image
    cv2.imshow('Image', img)

    key = cv2.waitKey(30)
    if key == 27: # 13 = enter, 27 = esc
        break