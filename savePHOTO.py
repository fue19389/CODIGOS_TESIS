# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

import os
import cv2
import math as mt
import numpy as np
import pandas as pd

class captura:

    def __init__(self):


# ------------------------------------------------
# ----- Seleccionar modelo -----------------------
# ------------------------------------------------

        self.nmodel = 6

# ------------------------------------------------
# ----- Directorios a utilizar -------------------
# ------------------------------------------------

        self.dirphoto = r'C:\Users\gerar\PycharmProjects\TRAINFACE'
        self.dirhold = r'C:\Users\gerar\PycharmProjects\PFOTOS'
        self.dirvrbls = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train.npy'

# ------------------------------------------------
# ----- Cantidad de labels base +1 ---------------
# ------------------------------------------------
        self.plen = 2083

# ------------------------------------------------
# ----- Funciones --------------------------------
# ------------------------------------------------

    def takePHOTO(self, tipo):

        if tipo == 1 or tipo == 4 or tipo == 7:
            self.pfxname = 'z_00_'
        if tipo == 2 or tipo == 5:
            self.pfxname = 'z_01_'
        if tipo == 3 or tipo == 6 or tipo == 9:
            self.pfxname = 'z_02_'
        if tipo == 8:
            self.pfxname = 'z_03_'

        # ------------------------------------------------
        # ----- Tomar, guardar y nombrar fotografía ------
        # ------------------------------------------------

        idx = 0
        pholist = os.listdir(self.dirphoto)
        holdlist = os.listdir(self.dirhold)
        for file in pholist:
            if file.startswith(self.pfxname):
                idx += 1
        for file in holdlist:
            if file.startswith(self.pfxname):
                idx += 1

        name = self.pfxname + str(int(idx + 1)) + '.jpg'

        # Take photo
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()

        savedir = os.path.join(self.dirhold, name)
        cv2.imwrite(savedir, frame)

# ------------------------------------------------
# ----- Simulacion de guardar foto ---------------
# ------------------------------------------------

    def loadD(self, do):

        if do == 1:

            # Mover archivos

            holdlist = os.listdir(self.dirhold)

            for file in holdlist:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirphoto, file)
                os.replace(oldpath, newpath)

            # Creación de labels
            lbl = []
            pholist = os.listdir(self.dirphoto)
            for file in pholist:
                if file.startswith('z_00'):
                    lbl.append(0)
                if file.startswith('z_01'):
                    lbl.append(1)
                if file.startswith('z_02'):
                    lbl.append(2)
                if file.startswith('z_03'):
                    lbl.append(3)

            # Enviar a archivo excel
            df = pd.DataFrame(list(zip(lbl)))
            with pd.ExcelWriter('facelabels.xlsx', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='traintags', header=False, index=False, startcol=self.nmodel, startrow=self.plen)

        if do != 1:
            pass



def main():

    camara = captura()

    poshead = int(input('Seleccione la posicion de cabeza: '))
    camara.takePHOTO(poshead)
    loaddat = int(input('¿Cargar datos? '))
    camara.loadD(loaddat)



if __name__ == '__main__':
    main()


