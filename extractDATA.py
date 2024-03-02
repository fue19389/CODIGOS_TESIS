# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

import os
import cv2
import numpy as np
import pandas as pd

# ------------------------------------------------
# ----- Seleccionar de datos ---------------------
# ------------------------------------------------

# 0 extrae imágenes, 1 extrae etiquetas
imglbl = 1

# 0 extrae grupo de entrenamiento, 1 extrae grupo de prueba
tsttrn = 1

# Si se escoge etiquetas, guardar para modelos 0 -> 6

lbl = 6

# ------------------------------------------------
# ----- Directorios a utilizar -------------------
# ------------------------------------------------

# Se selecciona el archivo .xlsx dentro del repositorio
lbldir = r"C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx"
# Directorio para guardar las variables a exportar
expordir = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS'
# Directorio para con carpetas de fotografias
imgdir = r'C:\Users\gerar\PycharmProjects'

# De esta manera solo se tienen que solicitar estos directorios y se aclara que
# las carpetas de fotografías se llaman TRAINFACE y TESTFACE
# El nombre de las variables exportadas aún lo tengo de manera fija

# ------------------------------------------------
# ----- Rutina extracción pixeles-----------------
# ------------------------------------------------

#Ahora se trabajará con el modelo 6 únicamente, cuando este listo sera el original nada mas
if imglbl == 0:

    if tsttrn == 0:
        foldname = 'TRAINFACE'
        xname = 'x_train6'
    if tsttrn == 1:
        foldname = 'TESTFACE'
        xname = 'x_test6'

    tdir = os.path.join(imgdir, foldname)
    xdir = os.path.join(expordir, xname)

    xlist = os.listdir(tdir)
    lenolist = int(len(np.array(xlist)))
    x_t = np.zeros((lenolist, 180, 320, 3))
    i = 0

    for filename in xlist:
        # if filename.endswith('.jpg'): / Esto solo aplica si hay mas de un tipo de archivos
        im = cv2.imread(os.path.join(tdir, filename))
        imr = cv2.resize(im, (320, 180))
        imr = cv2.cvtColor(imr, cv2.COLOR_BGR2RGB)
        x_t[i] = imr
        i = i + 1

    x_t = x_t.astype(int)
    np.save(xdir, x_t)


# ------------------------------------------------
# ----- Rutina extracción etiquetas---------------
# ------------------------------------------------
if imglbl == 1:


    # Las variables exportadas de etiquetas se guardan dependiento de la etiqueta
    if tsttrn == 0:
        sheet = 'traintags'
        if lbl == 0:
            col = 0
            yname = 'y_train'
        if lbl == 1:
            col = 1
            yname = 'y_train1'
        if lbl == 2:
            col = 2
            yname = 'y_train2'
        if lbl == 3:
            col = 3
            yname = 'y_train3'
        if lbl == 4:
            col = 4
            yname = 'y_train4'
        if lbl == 5:
            col = 5
            yname = 'y_train5'
        if lbl == 6:
            col = 6
            yname = 'y_train6'

    if tsttrn == 1:
        sheet = 'testtags'
        if lbl == 0:
            col = 0
            yname = 'y_test'
        if lbl == 1:
            col = 1
            yname = 'y_test1'
        if lbl == 2:
            col = 2
            yname = 'y_test2'
        if lbl == 3:
            col = 3
            yname = 'y_test3'
        if lbl == 4:
            col = 4
            yname = 'y_test4'
        if lbl == 5:
            col = 5
            yname = 'y_test5'
        if lbl == 6:
            col = 6
            yname = 'y_test6'

    ydir = os.path.join(expordir, yname)
    y_t = np.array(pd.read_excel(lbldir, sheet_name=sheet, index_col=col))
    y_t = y_t.astype(int)
    np.save(ydir, y_t)