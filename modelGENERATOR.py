# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np
import seaborn as sn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import SGD

# ------------------------------------------------
# ----- Seleccionar de datos ---------------------
# ------------------------------------------------

# Grupo de etiquetas a usar de 0 -> 5
# JUSTO AHORA SOLO SE PUEDE USAR EL 4 y 5!!!!!!!
ndat = 5

# ------------------------------------------------
# ----- Definición de tamaño de letra y figura----
# ------------------------------------------------
rcParams.update({'font.size': 12})
plt.rcParams['figure.figsize'] = [12, 12]

# ------------------------------------------------
# ----Extraer data previamente arreglada----------
# ------------------------------------------------

x_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\x_train4.npy') #TEMPORALMENTE SE CAMBIÓ LA VARIABLE
x_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\x_test.npy')   #PORQUE CAMBIE UNOS DATOS, DSPS LO ARREGLO

if ndat == 0:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA0'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM0'
    n_nodesal = 9
elif ndat == 1:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test1.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train1.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or1.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA1'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM1'
    n_nodesal = 9
elif ndat == 2:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test2.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train2.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or2.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA2'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM2'
    n_nodesal = 6
elif ndat == 3:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test3.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train3.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or3.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA3'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM3'
    n_nodesal = 6
elif ndat == 4:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test4.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train4.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or4.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA4'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM4'
    n_nodesal = 4
elif ndat == 5:
    y_test = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_test5.npy')
    y_train = np.load(r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train5.npy')
    dirmodel = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or5.keras'
    dirlossacc = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\LA5'
    dircm = r'C:\Users\gerar\Desktop\UVG\10semestre\TESIS\DOCUMENTO_TESIS\figures\CM5'
    n_nodesal = 3

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
plt.savefig(dirlossacc)
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
plt.savefig(dircm)
plt.show()


