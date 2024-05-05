import serial
import threading
import tensorflow as tf
import numpy as np
import cv2
import faceLANDMARKS as fL


class Use_BT_MODEL:
    def __init__(self):

        self.ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
        self.ho_model = tf.keras.models.load_model(self.ho_model)
        self.detector = fL.FaceMeshDetector()
        self.CAP = cv2.VideoCapture(0)


    def on(self):
        def run_on():

            try:
                self.BT = serial.Serial('COM4', 115200)
                print('Conexión exitosa')
            except:
                print('Error de conexión')

            while True:
                _, imgF = self.CAP.read()
                img, nodes = self.detector.findFaceMesh(imgF)
                nodes = np.array([nodes])
                if nodes.any() != 0:
                    y_predicted = self.ho_model.predict(nodes, verbose=None)
                    prediction = int(np.argmax(y_predicted))
                else:
                    prediction = 1
                self.BT.write(str(prediction).encode('utf-8'))

        on_thread = threading.Thread(target=run_on)
        on_thread.daemon = True
        on_thread.start()

    def stop(self):
        self.CAP.release()
        self.BT.close()
        cv2.destroyAllWindows()