import os
import cv2
import math as mt
import numpy as np
import pandas as pd


# Directiorios a utilizar
dirphoto = r'C:\Users\gerar\PycharmProjects\TRAINFACE'
dirhold = r'C:\Users\gerar\PycharmProjects\PFOTOS'
dirvrbls = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train.npy'

# proceso para guardar labels sin acceder al archivo
val = 2
y_ttrain = np.load(dirvrbls)
y_t = np.append(y_ttrain, val)

#proceso para guardar labels accediendo al archivo

# Setup
lbl = [None]*9



#Guardar fotos

# Setup

phoidx = 0
pholist = os.listdir(dirphoto)
for filename in pholist:
    if filename.startswith('z'):
        phoidx += 1
grpnmbr = str(int(mt.floor((phoidx / 9) + 1)))
pfxname = 'z'
while True:



    # Simulación de click
    captura = input('Seleccione la posicion de la cabeza (1-9): ')
    captura = int(captura)

    if 0 < captura < 10:
        # Take photo
        cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
        _, frame = cap.read()  # return a single frame in variable `frame`

        # Save photo and labels

        if captura == 1:
            sfxname = '01.jpg'
            lbl[0] = 0
        elif captura == 2:
            sfxname = '02.jpg'
            lbl[1] = 1
        elif captura == 3:
            sfxname = '03.jpg'
            lbl[2] = 2
        elif captura == 4:
            sfxname = '04.jpg'
            lbl[3] = 0
        elif captura == 5:
            sfxname = '05.jpg'
            lbl[4] = 1
        elif captura == 6:
            sfxname = '06.jpg'
            lbl[5] = 2
        elif captura == 7:
            sfxname = '07.jpg'
            lbl[6] = 0
        elif captura == 8:
            sfxname = '08.jpg'
            lbl[7] = 3
        elif captura == 9:
            sfxname = '09.jpg'
            lbl[8] = 2

        jnt = pfxname + grpnmbr + sfxname
        savedir = os.path.join(dirhold, jnt)
        cv2.imwrite(savedir, frame)
        print(lbl)


        # If complete, move or not, the files to the traning set
        usrlist = os.listdir(dirhold)
        if np.array(usrlist).size == 9: # Para la GUI seria bueno que abra el directorio
            move = int(input('Mover archivos?:'))
            if move == 1:
                for file in usrlist:
                    oldpath = os.path.join(dirhold, file)
                    newpath = os.path.join(dirphoto, file)
                    os.replace(oldpath, newpath)

                df = pd.DataFrame(list(zip(lbl)))
                with pd.ExcelWriter('facelabels.xlsx', mode='a') as writer:
                    df.to_excel(writer, sheet_name='traintags', header='PRUEBAAPPEND')
                break






