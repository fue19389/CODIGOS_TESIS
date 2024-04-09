from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sn
import tensorflow as tf
import os
import numpy as np
import pandas as pd
from tensorflow.keras import layers, Sequential

rcParams.update({'font.size': 12})
plt.rcParams['figure.figsize'] = [12, 12]

# Directorios
lbldir = r"C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx"
traindir = r"C:\Users\gerar\PycharmProjects\TRAINLIST"
testdir = r"C:\Users\gerar\PycharmProjects\TESTLIST"

# Extracción de datos
trainlist = os.listdir(traindir)
x_train = np.zeros((len(trainlist), 468, 2))
itn = 0
testlist = os.listdir(testdir)
x_test = np.zeros((len(testlist), 468, 2))
itt = 0
# Generación de variables
for file in trainlist:
    x_train[itn] = np.load(os.path.join(traindir, file))
    itn += 1
for file in testlist:
    x_test[itt] = np.load(os.path.join(testdir, file))
    itt += 1


# Extracción de etiquetas
# Extraer el archivo de etiquetas desde una columna de excel
y_t = np.array(pd.read_excel(lbldir, sheet_name='traintags', usecols='J').dropna())
# Convertir el archivo de etiquetas para reducir tamaño
y_train = y_t.astype(int)

# Extraer el archivo de etiquetas desde una columna de excel
y_t = np.array(pd.read_excel(lbldir, sheet_name='testtags', usecols='J').dropna())
# Convertir el archivo de etiquetas para reducir tamaño
y_test = y_t.astype(int)

# Extracción de matriz de adyacencia
admat = np.array([np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\admat.npy')])
admattest = np.zeros((len(y_test), 468, 468))
admattrain = np.zeros((len(y_train), 468, 468))
for i in range(len(y_train)):
    admattrain[i] = admat
for i in range(len(y_test)):
    admattest[i] = admat

print(x_train.shape, y_train.shape, admattrain.shape)
print(x_test.shape, y_test.shape, admattest.shape)

# Define the parameters
num_classes = 4  # Number of classes for graph classification
conv1_output_dim = 64
conv2_output_dim = 32
num_epochs = 10

# Define graph convolution layers
conv1 = layers.Conv1D(conv1_output_dim, kernel_size=1, activation='relu', input_shape=(468, 2))
conv2 = layers.Conv1D(conv2_output_dim, kernel_size=1, activation='relu')
# Define global pooling (mean pooling) layer
global_pooling = layers.GlobalAveragePooling1D()
# Define fully connected output layer
output_layer = layers.Dense(num_classes, activation='softmax')


# Define the GNN model using Keras Sequential API
model = Sequential([conv1, conv2, global_pooling, output_layer])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit([x_train, admattrain], y_train, validation_data=([x_test, admattest], y_test), epochs=num_epochs)

# Evaluate the model
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
# plt.savefig(savefig1)
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
# plt.savefig(savefig2)
plt.show()
