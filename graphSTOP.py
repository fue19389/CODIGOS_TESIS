# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código para generar el modelo de aprendizaje con datos de landmarks de Mediapipe

# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sn
import tensorflow as tf
import os
import numpy as np
import pandas as pd
from tensorflow.keras import layers, Sequential


class ModelGraphStop:

    def __init__(self):

        # ------------------------------------------------
        # ----- Definición de tamaño de letra y figura----
        # ------------------------------------------------
        rcParams.update({'font.size': 12})
        plt.rcParams['figure.figsize'] = [12, 12]

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------
        self.lbldir = r"C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx"
        self.traindir = r"C:\Users\gerar\PycharmProjects\TRAINMOUTH"
        self.testdir = r"C:\Users\gerar\PycharmProjects\TESTMOUTH"
        self.figtssdir = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures'

        self.col = 'M' # TIENE que ser la columna siguiente a la de graphMODEL.py

    def TrainModel(self):

        # ------------------------------------------------
        # ----Extracción de datos----------
        # ------------------------------------------------

        # TRAIN N TEST
        trainlist = os.listdir(self.traindir)
        x_train = np.zeros((len(trainlist), 40, 2))
        itn = 0
        testlist = os.listdir(self.testdir)
        x_test = np.zeros((len(testlist), 40, 2))
        itt = 0
        # Generación de variables
        for file in trainlist:
            x_train[itn] = np.load(os.path.join(self.traindir, file))
            itn += 1
        for file in testlist:
            x_test[itt] = np.load(os.path.join(self.testdir, file))
            itt += 1

        # LABELS
        # Extraer el archivo de etiquetas desde una columna de excel
        y_t = np.array(pd.read_excel(self.lbldir, sheet_name='traintags', usecols=self.col).dropna())
        # Convertir el archivo de etiquetas para reducir tamaño
        y_train = y_t.astype(int)

        # Extraer el archivo de etiquetas desde una columna de excel
        y_t = np.array(pd.read_excel(self.lbldir, sheet_name='testtags', usecols=self.col).dropna())
        # Convertir el archivo de etiquetas para reducir tamaño
        y_test = y_t.astype(int)

        # Adjacency Matrix
        admatlip = np.array([np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\admatlip.npy')])
        admattest = np.zeros((len(y_test), 468, 468))
        admattrain = np.zeros((len(y_train), 468, 468))
        for i in range(len(y_train)):
            admattrain[i] = admatlip
        for i in range(len(y_test)):
            admattest[i] = admatlip

        savefig1 = os.path.join(self.figtssdir, 'LA12M')
        savefig2 = os.path.join(self.figtssdir, 'CM12M')
        # ------------------------------------------------------
        # -----Generación de modelo ----------------------------
        # ------------------------------------------------------

        # Parameters
        num_classes = 2
        conv1_output_dim = 75
        conv2_output_dim = 150
        conv3_output_dim = 75
        num_epochs = 5

        # Layers
        conv1 = layers.Conv1D(conv1_output_dim, kernel_size=2, activation='relu', input_shape=(40, 2))
        conv2 = layers.Conv1D(conv2_output_dim, kernel_size=4, activation='relu')
        conv3 = layers.Conv1D(conv3_output_dim, kernel_size=2, activation='relu')
        global_pooling = layers.GlobalAveragePooling1D()
        output_layer = layers.Dense(num_classes, activation='softmax')
        model = Sequential([conv1, conv2, conv3, global_pooling, output_layer])

        # ------------------------------------------------------
        # ----Compilar, entrenar, evaluar modelo----------------
        # ------------------------------------------------------

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        history = model.fit([x_train, admattrain], y_train, validation_data=([x_test, admattest], y_test),
                            epochs=num_epochs)
        model.save(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12M.keras')

        _, actual_acc = model.evaluate([x_test, admattest], y_test)

        # ------------------------------------------------------
        # ----GRAFICAS LOSS Y ACCURACY: TEST, TRAIN-------------
        # ------------------------------------------------------
        plt.subplot(211)
        plt.title('Loss')
        plt.plot(history.history['loss'], label='train')
        plt.plot(history.history['val_loss'], label='test')
        plt.xlabel('Epochs')
        plt.legend()

        plt.subplot(212)
        plt.title('Accuracy')
        plt.plot(history.history['accuracy'], label='train')
        plt.plot(history.history['val_accuracy'], label='test')
        plt.xlabel('Epochs')
        plt.legend()
        plt.savefig(savefig1)
        plt.show()

        # -----------------------------------------------------
        # ----Predict del modelo completo ---------------------
        # -----------------------------------------------------

        y_predicted_full = model.predict(x_test, verbose=2)
        prediction_labels = np.zeros_like(y_test)
        for i in range(len(x_test)):
            prediction_labels[i] = np.argmax(y_predicted_full[i])

        # -----------------------------------------------------
        # ----Matriz de confusión -----------------------------
        # -----------------------------------------------------

        y_test = np.squeeze(y_test)
        prediction_labels = np.squeeze(prediction_labels)
        cm = tf.math.confusion_matrix(labels=y_test, predictions=prediction_labels)

        plt.figure(figsize=(10, 7))
        sn.heatmap(cm, annot=True, fmt='d')
        plt.xlabel('Predicted')
        plt.ylabel('Truth')
        plt.savefig(savefig2)
        plt.show()

# if __name__ == '__main__':
#     main()

