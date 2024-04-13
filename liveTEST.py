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



         
    def on(self):


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
        elif self.n_model == 7:
            self.mname = 'head_or7.keras'
        elif self.n_model == 8:
            self.mname = 'head_or8.keras'
        elif self.n_model == 9:
            self.mname = 'head_or9.keras'
        elif self.n_model == 10:
            self.mname = 'head_or10.keras'
        elif self.n_model == 11:
            self.mname = 'head_or11.keras'
        elif self.n_model == 12:
            self.mname = 'head_or12.keras'

        self.ho_model = os.path.join(self.expordir, self.mname)
        self.ho_model = tf.keras.models.load_model(self.ho_model)

        # -----------------------------------------------------
        # ---------Inicialización de la Webcam---- ------------
        # -----------------------------------------------------

        self.cap = cv2.VideoCapture(0)
        ttl.TurtleScreen._RUNNING = True
        self.leo = ttl.Turtle()
        detector = fL.FaceMeshDetector()
        self.admat = np.array([np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\admat.npy')])
        cont = 0
        conta = 0
        contb = 0
        flag = 0

        # -----------------------------------------------------
        # ----Visualizar movimiento de turtle -----------------
        # -----------------------------------------------------

        while True:
        
            # Saving captured image and transforming from BGR TO RGB

            _, imgF = self.cap.read()
            img, nodes = detector.findFaceMesh(imgF)
            nodes = np.array([nodes])
            if nodes.any() != 0:
                y_predicted = self.ho_model.predict(nodes, verbose=0)
                prediction = int(np.argmax(y_predicted))
            else:
                prediction = 1


            if prediction == 0:
                self.leo.left(7)
                self.leo.forward(conta)
                self.leo.backward(contb)

            if prediction == 1:
                self.leo.forward(conta)
                self.leo.backward(contb)
                flag = 0
            if prediction == 2:
                self.leo.right(7)
                self.leo.forward(conta)
                self.leo.backward(contb)


            if prediction == 3:
                if flag == 0:
                    cont += 1
                    if cont > -1 and cont < 5:
                        conta = int(cont)
                    if cont < 1 and cont > -5:
                        contb = int(-1*cont)
                    if cont > 4:
                        conta = int(4)
                        cont = 4
                    if cont < -4:
                        contb = int(4)
                        cont = -4
                    flag = 1
                else:
                    pass

            if prediction == 4:
                if flag == 0:
                    cont -= 1
                    if cont > -1 and cont < 5:
                        conta = int(cont)
                    if cont < 1 and cont > -5:
                        contb = int(-1*cont)
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
            print('p f c a b')
            print(prediction, flag, cont, conta, contb)

            # Show the complete image
            cv2.imshow('Image', img)
        
            # key = cv2.waitKey(5)
            # if key == 27: # 13 = enter, 27 = esc

    def stop(self):
        self.cap.release()
        ttl.bye()
        cv2.destroyAllWindows()




