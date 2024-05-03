import serial
import tensorflow as tf
import numpy as np
import cv2
import faceLANDMARKS as fL

CAP = cv2.VideoCapture(0)
ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
ho_model = tf.keras.models.load_model(ho_model)
detector = fL.FaceMeshDetector()
flag = 0

try:
    BT = serial.Serial('COM4', 115200)
    print('Conexión exitosa')
except:
    print('Error de la conexión')
while True:
    mensaje = input('Ingrese un valor 0 o 1: ')
    BT.write(mensaje.encode('utf-8'))

# while True:
#
#     esp = serial.Serial('COM4',9600)
#     _, imgF = CAP.read()
#     img, nodes = detector.findFaceMesh(imgF)
#     nodes = np.array([nodes])
#     if nodes.any() != 0:
#        y_predicted = ho_model.predict(nodes, verbose=None)
#        prediction = int(np.argmax(y_predicted))
#     else:
#        prediction = 1
#
#     esp.write((r'1\n').encode())
