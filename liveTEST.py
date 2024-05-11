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


class UseModel:

    def __init__(self):
        # ------------------------------------------------------
        # -----------------Selección de modelo------------------
        # ------------------------------------------------------

        # Actualmente, se tienen modelos del 0 -> 8
        self.n_model = 12

        # -----------------------------------------------------

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------

        # Directorio para guardar las variables a exportar
        self.expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'

        # detector de landmarks
        self.detector = fL.FaceMeshDetector()
        # predicción incial
        self.prediction = 1
        self.lipdif = 0.0


    # -----------------------------------------------------
    # -------------------Cargar modelo---------------------
    # -----------------------------------------------------

    def load_model(self):

        if self.n_model in range(13):
            self.mname = f'head_or{self.n_model}.keras'
            self.ho_model = os.path.join(self.expordir, self.mname)
            self.ho_model = tf.keras.models.load_model(self.ho_model)
        else:
            raise ValueError("Invalid model number")

    # -----------------------------------------------------
    # -------------------Predicción de modelo---------------------
    # -----------------------------------------------------
    def or_predict(self, imgOG, predict0):

        # Perform face detection using the FaceMeshDetector

        img, nodes = self.detector.findFaceMesh(imgOG)
        nodes = np.array([nodes])
        # Check if any face landmarks were detected
        if nodes.any() != 0:
            xlip = (nodes[0][13][0]) - (nodes[0][14][0])
            ylip = (nodes[0][13][1]) - (nodes[0][14][1])
            lipdif = ((xlip**2)+(ylip**2))**0.5
            y_predicted = self.ho_model.predict(nodes, verbose=0)
            prediction = int(np.argmax(y_predicted))
        else:
            prediction = predict0
            lipdif = 0.0

        return prediction, lipdif

    def on(self):
        # -----------------------------------------------------
        # ---------Inicialización de la Webcam---- ------------
        # -----------------------------------------------------
        cont = 0
        conta = 0
        contb = 0
        flag = 0

        self.load_model()
        self.cap = cv2.VideoCapture(0)
        ttl.TurtleScreen._RUNNING = True
        self.leo = ttl.Turtle()

        # -----------------------------------------------------
        # ----Visualizar movimiento de turtle -----------------
        # -----------------------------------------------------

        while True:

            # Saving captured image
            _, img = self.cap.read()
            self.prediction, self.lipdif = self.or_predict(img, self.prediction)

            # cv2.imshow('Image', img)
            # cv2.waitKey(1) #This helps the program to not stop

            if self.lipdif < 0.03:
                if self.prediction == 0:
                    self.leo.left(7)
                    self.leo.forward(conta)
                    self.leo.backward(contb)

                if self.prediction == 1:
                    self.leo.forward(conta)
                    self.leo.backward(contb)
                    flag = 0
                if self.prediction == 2:
                    self.leo.right(7)
                    self.leo.forward(conta)
                    self.leo.backward(contb)

                if self.prediction == 3:

                    if flag == 0:
                        cont += 1
                        if cont > -1 and cont < 5:
                            conta = int(cont)
                        if cont < 1 and cont > -5:
                            contb = int(-1 * cont)
                        if cont > 4:
                            conta = int(4)
                            cont = 4
                        if cont < -4:
                            contb = int(4)
                            cont = -4
                        flag = 1
                    else:
                        pass

                if self.prediction == 4:

                    if flag == 0:
                        cont -= 1
                        if cont > -1 and cont < 5:
                            conta = int(cont)
                        if cont < 1 and cont > -5:
                            contb = int(-1 * cont)
                        if cont > 4:
                            conta = int(4)
                            cont = 4
                        if cont < -4:
                            contb = int(4)
                            cont = -4
                        flag = 1
                    else:
                        pass

                else:
                    pass
                print('p f c a b SN')
                print(self.prediction, flag, cont, conta, contb, self.lipdif)

            elif self.lipdif >= 0.03:
                print('stop')
                self.leo.forward(0)
                self.leo.backward(0)
                cont = 0
                conta = 0
                contb = 0
                flag = 0

        self.cap.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.cap.release()
        ttl.bye()
        cv2.destroyAllWindows()




