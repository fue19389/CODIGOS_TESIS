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
import time
import numpy as np
import pygame as pg
import pandas as pd
import faceLANDMARKS as fL


class ModelFeeder:

    def __init__(self):

        # ------------------------------------------------
        # ----- Seleccionar modelo -----------------------
        # ------------------------------------------------

        # Escoge la columna de la data en el archivo excel
        self.nmodel = 9

        # ------------------------------------------------
        # ----- Directorios a utilizar -------------------
        # ------------------------------------------------

        self.dirtrain = r'C:\Users\gerar\PycharmProjects\TRAINLIST'
        self.dirtest = r'C:\Users\gerar\PycharmProjects\TESTLIST'
        self.dirhold = r'C:\Users\gerar\PycharmProjects\PFOTOS'
        self.dirxlsx = r'C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\facelabels.xlsx'


        # ------------------------------------------------
        # ----- Sonidos a utilizar -------------------
        # ------------------------------------------------

        # Sonidos obtenidos de: https://sfxr.me/
        pg.init()
        self.s1 = pg.mixer.Sound('1st.wav')
        self.s2 = pg.mixer.Sound('2nd.wav')
        self.s3 = pg.mixer.Sound('3rd.wav')
        self.sf = pg.mixer.Sound('last.wav')

        # ------------------------------------------------
        # ----- Obtener Landmarks -------------------
        # ------------------------------------------------

        self.detector = fL.FaceMeshDetector()


    # ------------------------------------------------
    # ----- Tomar y nombrar fotos  -------------------
    # ------------------------------------------------
    def takePHOTO(self):

        # First run of photos
        starttime = time.time()
        # Sound to prepare
        self.s1.play()
        pg.time.delay(750)
        self.s2.play()
        pg.time.delay(750)
        self.s3.play()
        cap = cv2.VideoCapture(0)
        while True:
            # Getting landmarks
            _, frame = cap.read()
            _, nodes = self.detector.findFaceMesh(frame)

            self.pfxname = 'z_00_'
            idx = 0
            trainlist = os.listdir(self.dirtrain)
            testlist = os.listdir(self.dirtest)
            holdlist = os.listdir(self.dirhold)

            for file in trainlist:
                if file.startswith(self.pfxname) and file.endswith('.npy'):
                    idx += 1
            for file in testlist:
                if file.startswith(self.pfxname) and file.endswith('.npy'):
                    idx += 1
            for file in holdlist:
                if file.startswith(self.pfxname) and file.endswith('.npy'):
                    idx += 1

            # Saving process
            if len(nodes) != 0:
                # Landmarks
                name = self.pfxname + str(int(idx + 1))
                savedat = os.path.join(self.dirhold, name)
                np.save(savedat, nodes)
                # Images
                name = name + '.jpg'
                savedir = os.path.join(self.dirhold, name)
                cv2.imwrite(savedir, frame)
            elif len(nodes) == 0:
                pass

            if time.time() - starttime > 8:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # # Second run of photos
        # starttime = time.time()
        #
        # # Sound to prepare
        # self.s1.play()
        # pg.time.delay(750)
        # self.s2.play()
        # pg.time.delay(750)
        # self.s3.play()
        # cap = cv2.VideoCapture(0)
        #
        # while True:
        #     _, frame = cap.read()
        #     self.pfxname = 'z_01_'
        #     idx = 0
        #     trainlist = os.listdir(self.dirtrain)
        #     testlist = os.listdir(self.dirtest)
        #     holdlist = os.listdir(self.dirhold)
        #
        #     for file in trainlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in testlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in holdlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #
        #     name = self.pfxname + str(int(idx + 1)) + '.jpg'
        #     savedir = os.path.join(self.dirhold, name)
        #     cv2.imwrite(savedir, frame)
        #
        #     if time.time() - starttime > 8:
        #         self.sf.play()
        #         pg.time.delay(2000)
        #         cv2.destroyAllWindows()
        #         break
        #     pass
        #
        # # Third run of photos
        # starttime = time.time()
        #
        # # Sound to prepare
        # self.s1.play()
        # pg.time.delay(750)
        # self.s2.play()
        # pg.time.delay(750)
        # self.s3.play()
        # cap = cv2.VideoCapture(0)
        # while True:
        #     _, frame = cap.read()
        #     self.pfxname = 'z_02_'
        #     idx = 0
        #     trainlist = os.listdir(self.dirtrain)
        #     testlist = os.listdir(self.dirtest)
        #     holdlist = os.listdir(self.dirhold)
        #
        #     for file in trainlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in testlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in holdlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #
        #     name = self.pfxname + str(int(idx + 1)) + '.jpg'
        #     savedir = os.path.join(self.dirhold, name)
        #     cv2.imwrite(savedir, frame)
        #
        #     if time.time() - starttime > 8:
        #         self.sf.play()
        #         pg.time.delay(2000)
        #         cv2.destroyAllWindows()
        #         break
        #     pass
        #
        # # Fourth run of photos
        # starttime = time.time()
        #
        # # Sound to prepare
        # self.s1.play()
        # pg.time.delay(750)
        # self.s2.play()
        # pg.time.delay(750)
        # self.s3.play()
        # cap = cv2.VideoCapture(0)
        # while True:
        #     _, frame = cap.read()
        #     self.pfxname = 'z_03_'
        #     idx = 0
        #     trainlist = os.listdir(self.dirtrain)
        #     testlist = os.listdir(self.dirtest)
        #     holdlist = os.listdir(self.dirhold)
        #
        #     for file in trainlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in testlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #     for file in holdlist:
        #         if file.startswith(self.pfxname):
        #             idx += 1
        #
        #     name = self.pfxname + str(int(idx + 1)) + '.jpg'
        #     savedir = os.path.join(self.dirhold, name)
        #     cv2.imwrite(savedir, frame)
        #
        #     if time.time() - starttime > 8:
        #         self.sf.play()
        #         pg.time.delay(750)
        #         cv2.destroyAllWindows()
        #         break
        #     pass

        os.startfile(filepath=self.dirhold)
    # ------------------------------------------------
    # ----- Cargar fotos al sistema ------------------
    # ------------------------------------------------

    def loadD(self, tsttrn):

        tsttrn = int(tsttrn)

        # Selección de carga a test o train, con su respectiva fila de inicio
        if tsttrn == 0:
            shtnm = 'traintags'
            strtrw = 1
            dirtrgt = self.dirtrain
        elif tsttrn == 1:
            shtnm = 'testtags'
            strtrw = 1
            dirtrgt = self.dirtest
        else:
            pass

        # Mover archivos
        holdlist = os.listdir(self.dirhold)
        for file in holdlist:
            if file.endswith('.npy'):
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

    def eraseSERIES(self):
        # Borrar archivos
        holdlist = os.listdir(self.dirhold)

        for file in holdlist:
            path = os.path.join(self.dirhold, file)
            os.remove(path)

    # ------------------------------------------------
    # ----- Borrar fotos de directorio temp-----------
    # ------------------------------------------------

    def resetMaster(self, tsttrn):

        # Selección de carga a test o train, con su respectiva fila de inicio
        if tsttrn == 0:
            shtnm = 'traintags'
            strtrw = 1
            dirtrgt = self.dirtrain
        elif tsttrn == 1:
            shtnm = 'testtags'
            strtrw = 1
            dirtrgt = self.dirtest
        else:
            pass

        # Borrar archivos
        idx = 0
        filelist = os.listdir(dirtrgt)
        for file in filelist:
            if file.startswith('z_'):
                path = os.path.join(dirtrgt, file)
                os.remove(path)
                idx += 1


        # Borrar etiquetas del excel
        lbl = [None]*idx
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=shtnm, header=False, index=False, startcol=self.nmodel, startrow=strtrw)










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
