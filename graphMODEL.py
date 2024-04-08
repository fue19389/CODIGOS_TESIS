import tensorflow as tf
import dgl
import os
import numpy as np
import pandas as pd
from tensorflow.keras import layers, Sequential



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


print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)





#
# # Define the parameters
# num_classes = 4  # Number of classes for graph classification
# conv1_output_dim = 64
# conv2_output_dim = 32
#
# # Define placeholders for inputs and adjacency matrices
# inputs = tf.keras.Input(shape=(None, None))  # Shape: (batch_size, num_nodes, num_features)
# adjacency_matrices = tf.keras.Input(shape=(None, None))  # Shape: (batch_size, num_nodes, num_nodes)
#
# # Create DGL Graphs
# graphs = []
# for i in range(len(inputs)):
#     g = dgl.graph(adjacency_matrices[i])
#     g.ndata['feat'] = inputs[i]
#     graphs.append(g)
#
# # Define graph convolution layers using DGL
# conv1 = dgl.nn.GraphConv(conv1_output_dim, 'relu')
# conv2 = dgl.nn.GraphConv(conv2_output_dim, 'relu')
#
# # Define global pooling (mean pooling) layer
# global_pooling = layers.GlobalAveragePooling1D()
#
# # Define fully connected output layer
# output_layer = layers.Dense(num_classes, activation='softmax')
#
# # Define the model using Sequential API
# model = Sequential([
#     layers.Lambda(lambda x: [conv1(graphs[i], x[i]) for i in range(len(x))]),  # Graph convolution 1
#     layers.Lambda(lambda x: [conv2(graphs[i], x[i]) for i in range(len(x))]),  # Graph convolution 2
#     global_pooling,
#     output_layer
# ])
#
# # Compile the model
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# # Prepare the data (replace with your actual data)
# X_train = np.random.rand(batch_size, num_nodes, num_features)
# adjacency_matrices_train = np.random.randint(2, size=(batch_size, num_nodes, num_nodes))
# y_train = np.random.randint(num_classes, size=batch_size)
#
# # Train the model
# model.fit([X_train, adjacency_matrices_train], y_train, epochs=num_epochs, batch_size=batch_size)
