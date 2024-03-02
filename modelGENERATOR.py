# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np
import seaborn as sn
import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras.optimizers import SGD

# ------------------------------------------------
# ----- Seleccionar de datos ---------------------
# ------------------------------------------------

# Grupo de etiquetas a usar de 0 -> 5
# Ahora las pruebas requieren usar el 6, que es copia del 4 pero con el sistema de agregar fotos
ndat = 6

# ------------------------------------------------
# ----- Definición de tamaño de letra y figura----
# ------------------------------------------------
rcParams.update({'font.size': 12})
plt.rcParams['figure.figsize'] = [12, 12]

# ------------------------------------------------
# ----- Directorios a utilizar -------------------
# ------------------------------------------------

# Directorio para guardar las variables a exportar
expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'
# Directorio de imagenes de la tesis en textudio
figtssdir = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures'

# ------------------------------------------------
# ----Extraer data previamente arreglada----------
# ------------------------------------------------

x_tn = 'x_train.npy'
x_tt = 'x_test.npy'
x_tn = os.path.join(expordir, x_tn)
x_tt = os.path.join(expordir, x_tt)
x_train = np.load(x_tn)
x_test = np.load(x_tt)

if ndat == 0:
    y_tt = 'y_test.npy'
    y_tn = 'y_train.npy'
    mname = 'head_or.keras'
    losacfig = 'LA0'
    cmfig = 'CM0'
    n_nodesal = 9
elif ndat == 1:
    y_tt = 'y_test1.npy'
    y_tn = 'y_train1.npy'
    mname = 'head_or1.keras'
    losacfig = 'LA1'
    cmfig = 'CM1'
    n_nodesal = 9
elif ndat == 2:
    y_tt = 'y_test2.npy'
    y_tn = 'y_train2.npy'
    mname = 'head_or2.keras'
    losacfig = 'LA2'
    cmfig = 'CM2'
    n_nodesal = 6
elif ndat == 3:
    y_tt = 'y_test3.npy'
    y_tn = 'y_train3.npy'
    mname = 'head_or3.keras'
    losacfig = 'LA3'
    cmfig = 'CM3'
    n_nodesal = 6
elif ndat == 4:
    y_tt = 'y_test4.npy'
    y_tn = 'y_train4.npy'
    mname = 'head_or4.keras'
    losacfig = 'LA4'
    cmfig = 'CM4'
    n_nodesal = 4
elif ndat == 5:
    y_tt = 'y_test5.npy'
    y_tn = 'y_train5.npy'
    mname = 'head_or5.keras'
    losacfig = 'LA5'
    cmfig = 'CM5'
    n_nodesal = 3
elif ndat == 6:
    y_tt = 'y_test6.npy'
    y_tn = 'y_train6.npy'
    mname = 'head_or6.keras'
    losacfig = 'LA6'
    cmfig = 'CM6'
    n_nodesal = 4

y_tn = os.path.join(expordir, y_tn)
y_tt = os.path.join(expordir, y_tt)
y_test = np.load(y_tt)
y_train = np.load(y_tn)

dirmodel = os.path.join(expordir, mname)
savefig1 = os.path.join(figtssdir, losacfig)
savefig2 = os.path.join(figtssdir, cmfig)

# --------------------------------------------------
# ----Normalizar datos -----------------------------
# --------------------------------------------------

x_train = x_train / 255
x_test = x_test / 255

# ------------------------------------------------------
# -----Generación de modelo ----------------------------
# ------------------------------------------------------

layer0 = tf.keras.layers.Conv2D(10, (3, 3), activation='relu', input_shape=(180, 320, 3))
layer1 = tf.keras.layers.MaxPooling2D(2)
layer2 = tf.keras.layers.Flatten()
# layer3 = tf.keras.layers.Dropout(0.5)
layer4 = tf.keras.layers.Dense(75, activation='relu')
layer5 = tf.keras.layers.Dense(150, activation='relu')
layer6 = tf.keras.layers.Dense(75, activation='relu')
# layern = tf.keras.layers.Dense(100, activation='relu')
layer7 = tf.keras.layers.Dense(n_nodesal, activation='softmax')
model = tf.keras.Sequential([layer0, layer1, layer2, layer4, layer5, layer7])

# ------------------------------------------------------
# ----Compilar, entrenar, evaluar modelo----------------
# ------------------------------------------------------

# optimizer = SGD(learning_rate=0.01, momentum=0.9)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)
model.save(dirmodel)

_, actual_acc = model.evaluate(x_test, y_test)

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


