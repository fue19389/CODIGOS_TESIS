# ------------------------------------------------
# ------------- Datos Generales ------------------
# ------------------------------------------------

# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Electrónica, Mecatrónica y Biomédica
# Gerardo Andres Fuentes Bámaca
# 19389
# Código para realizar la captura de nuevas imágenes y guardarlas

# ------------------------------------------------
# ----- Librerías a utilizar ---------------------
# ------------------------------------------------

import os
import cv2
import pandas as pd


class ModelFeeder:

    def __init__(self):

        # ------------------------------------------------
        # ----- Seleccionar modelo -----------------------
        # ------------------------------------------------

        # Escoge la columna de la data en el archivo excel
        self.nmodel = 6

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------

        self.dirtrain = r'C:\Users\gerar\PycharmProjects\TRAINFACE'
        self.dirtest = r'C:\Users\gerar\PycharmProjects\TESTFACE'
        self.dirhold = r'C:\Users\gerar\PycharmProjects\PFOTOS'
        self.dirxlsx = r'C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx'

    # ------------------------------------------------
    # ----- Tomar y nombrar fotos  -------------------
    # ------------------------------------------------
    def takePHOTO(self, hpos):

        hpos = int(hpos)

        # Take photo
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            # Show the complete image
            cv2.imshow('Image', frame)
            key = cv2.waitKey(30)
            if key == 13:
                break

        if key == 13:  # 13 = enter, 27 = esc

            if hpos == 1 or hpos == 4 or hpos == 7:
                self.pfxname = 'z_00_'
            if hpos == 2 or hpos == 5:
                self.pfxname = 'z_01_'
            if hpos == 3 or hpos == 6 or hpos == 9:
                self.pfxname = 'z_02_'
            if hpos == 8:
                self.pfxname = 'z_03_'

            # ------------------------------------------------
            # ----- Tomar, guardar y nombrar fotografía ------
            # ------------------------------------------------

            idx = 0
            trainlist = os.listdir(self.dirtrain)
            testlist = os.listdir(self.dirtest)
            holdlist = os.listdir(self.dirhold)
            for file in trainlist:
                if file.startswith(self.pfxname):
                    idx += 1
            for file in testlist:
                if file.startswith(self.pfxname):
                    idx += 1
            for file in holdlist:
                if file.startswith(self.pfxname):
                    idx += 1

            name = self.pfxname + str(int(idx + 1)) + '.jpg'
            savedir = os.path.join(self.dirhold, name)
            cv2.imwrite(savedir, frame)
            os.startfile(filepath=self.dirhold)

    # ------------------------------------------------
    # ----- Cargar fotos al sistema ------------------
    # ------------------------------------------------

    def loadD(self, tsttrn):

        tsttrn = int(tsttrn)

        # Selección de carga a test o train, con su respectiva columna de inicio
        if tsttrn == 1:
            shtnm = 'traintags'
            strtrw = 2083
            dirtrgt = self.dirtrain
        elif tsttrn == 2:
            shtnm = 'testags'
            strtrw = 745
            dirtrgt = self.dirtest
        else:
            pass

        # Mover archivos
        holdlist = os.listdir(self.dirhold)
        for file in holdlist:
            oldpath = os.path.join(self.dirhold, file)
            newpath = os.path.join(dirtrgt, file)
            os.replace(oldpath, newpath)

        # Creación de labels
        lbl = []
        filelist = os.listdir(dirtrgt)
        for file in filelist:
            if file.startswith('z_00'):
                lbl.append(0)
            elif file.startswith('z_01'):
                lbl.append(1)
            elif file.startswith('z_02'):
                lbl.append(2)
            elif file.startswith('z_03'):
                lbl.append(3)
            else:
                pass

        # Enviar a archivo excel
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=shtnm, header=False, index=False, startcol=self.nmodel, startrow=strtrw)

    # ------------------------------------------------
    # ----- Borrar fotos de directorio temp-----------
    # ------------------------------------------------

    def eraseD(self):
        # Borrar archivos
        holdlist = os.listdir(self.dirhold)

        for file in holdlist:
            path = os.path.join(self.dirhold, file)
            os.remove(path)

    # ------------------------------------------------
    # ----- Borrar fotos de directorio temp-----------
    # ------------------------------------------------

    def resetM(self):
        # Borrar archivos
        trainlist = os.listdir(self.dirtrain)

        for file in trainlist:
            path = os.path.join(self.dirtrain, file)
            os.remove(path)








# def main():
#
#     camara = captura()
#
#     poshead = int(input('Seleccione la posicion de cabeza: '))
#     camara.takePHOTO(poshead)
#     loaddat = int(input('¿Cargar datos? '))
#     if loaddat == 1:
#         camara.loadD()
#     elif loaddat != 1:
#         pass
#     erase = int(input('¿Borrar datos? '))
#     if erase == 1:
#         camara.eraseD()
#     elif erase != 1:
#         pass
#
#
# if __name__ == '__main__':
#     main()
