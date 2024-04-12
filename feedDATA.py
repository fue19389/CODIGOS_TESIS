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
import math
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
        self.nmodel = 13

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
        self.s1.set_volume(0.5)
        self.s2 = pg.mixer.Sound('2nd.wav')
        self.s2.set_volume(0.5)
        self.s3 = pg.mixer.Sound('3rd.wav')
        self.s3.set_volume(0.5)
        self.sf = pg.mixer.Sound('last.wav')
        self.sf.set_volume(0.5)

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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Second run of photos
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

            self.pfxname = 'z_01_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # 3rd run of photos
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

            self.pfxname = 'z_02_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Fourth run of photos
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

            self.pfxname = 'z_03_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Fifth run of photos
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

            self.pfxname = 'z_04_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Sixth run of photos
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

            self.pfxname = 'z_05_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Seventh run of photos
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

            self.pfxname = 'z_06_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Eigth run of photos
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

            self.pfxname = 'z_07_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        # Nineth run of photos
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

            self.pfxname = 'z_08_'
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

            if time.time() - starttime > 15:
                self.sf.play()
                pg.time.delay(2000)
                cv2.destroyAllWindows()
                break
            pass

        os.startfile(filepath=self.dirhold)
    # ------------------------------------------------
    # ----- Cargar fotos al sistema ------------------
    # ------------------------------------------------

    def loadD(self):

        # Prepare index to separate train and test
        i0 = 0
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        i5 = 0
        i6 = 0
        i7 = 0
        i8 = 0

        filelist = os.listdir(self.dirhold)
        for file in filelist:
            if file.startswith('z_00') and file.endswith('.npy'):
                i0 += 1
            elif file.startswith('z_01') and file.endswith('.npy'):
                i1 += 1
            elif file.startswith('z_02') and file.endswith('.npy'):
                i2 += 1
            elif file.startswith('z_03') and file.endswith('.npy'):
                i3 += 1
            elif file.startswith('z_04') and file.endswith('.npy'):
                i4 += 1
            elif file.startswith('z_05') and file.endswith('.npy'):
                i5 += 1
            elif file.startswith('z_06') and file.endswith('.npy'):
                i6 += 1
            elif file.startswith('z_07') and file.endswith('.npy'):
                i7 += 1
            elif file.startswith('z_08') and file.endswith('.npy'):
                i8 += 1
            else:
                pass

        i0 = int(math.ceil(i0*0.7))
        i1 = int(math.ceil(i1*0.7))
        i2 = int(math.ceil(i2*0.7))
        i3 = int(math.ceil(i3*0.7))
        i4 = int(math.ceil(i4*0.7))
        i5 = int(math.ceil(i5*0.7))
        i6 = int(math.ceil(i6*0.7))
        i7 = int(math.ceil(i7*0.7))
        i8 = int(math.ceil(i8*0.7))

        # Mover archivos a train y test
        ip0 = 0
        ip1 = 0
        ip2 = 0
        ip3 = 0
        ip4 = 0
        ip5 = 0
        ip6 = 0
        ip7 = 0
        ip8 = 0

        holdlist = os.listdir(self.dirhold)
        for file in holdlist:
            if file.startswith('z_00') and file.endswith('.npy') and ip0 < i0:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip0 += 1

            if file.startswith('z_01') and file.endswith('.npy') and ip1 < i1:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip1 += 1

            if file.startswith('z_02') and file.endswith('.npy') and ip2 < i2:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip2 += 1

            if file.startswith('z_03') and file.endswith('.npy') and ip3 < i3:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip3 += 1
            if file.startswith('z_04') and file.endswith('.npy') and ip4 < i4:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip4 += 1
            if file.startswith('z_05') and file.endswith('.npy') and ip5 < i5:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip5 += 1
            if file.startswith('z_06') and file.endswith('.npy') and ip6 < i6:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip6 += 1
            if file.startswith('z_07') and file.endswith('.npy') and ip7 < i7:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip7 += 1
            if file.startswith('z_08') and file.endswith('.npy') and ip8 < i8:
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtrain, file)
                os.replace(oldpath, newpath)
                ip8 += 1

        holdlist = os.listdir(self.dirhold)
        for file in holdlist:
            if file.endswith('.npy'):
                oldpath = os.path.join(self.dirhold, file)
                newpath = os.path.join(self.dirtest, file)
                os.replace(oldpath, newpath)

        # Creación de labels TRAIN
        lbl = []
        filelist = os.listdir(self.dirtrain)
        for file in filelist:
            if file.startswith('z_00'):
                lbl.append(0)
            elif file.startswith('z_01'):
                lbl.append(1)
            elif file.startswith('z_02'):
                lbl.append(2)
            elif file.startswith('z_03'):
                lbl.append(3)
            elif file.startswith('z_04'):
                lbl.append(4)
            elif file.startswith('z_05'):
                lbl.append(5)
            elif file.startswith('z_06'):
                lbl.append(6)
            elif file.startswith('z_07'):
                lbl.append(7)
            elif file.startswith('z_08'):
                lbl.append(8)
            else:
                pass


        # Enviar a archivo excel
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='traintags', header=False, index=False, startcol=self.nmodel, startrow=1)

        # Creación de labels TEST
        lbl = []
        filelist = os.listdir(self.dirtest)
        for file in filelist:
            if file.startswith('z_00'):
                lbl.append(0)
            elif file.startswith('z_01'):
                lbl.append(1)
            elif file.startswith('z_02'):
                lbl.append(2)
            elif file.startswith('z_03'):
                lbl.append(3)
            elif file.startswith('z_04'):
                lbl.append(4)
            elif file.startswith('z_05'):
                lbl.append(5)
            elif file.startswith('z_06'):
                lbl.append(6)
            elif file.startswith('z_07'):
                lbl.append(7)
            elif file.startswith('z_08'):
                lbl.append(8)
            else:
                pass

        # Enviar a archivo excel
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='testtags', header=False, index=False, startcol=self.nmodel, startrow=1)


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

    def resetMaster(self):

        # Borrar TRAIN
        idx = 0
        filelist = os.listdir(self.dirtrain)
        for file in filelist:
            if file.startswith('z_'):
                path = os.path.join(self.dirtrain, file)
                os.remove(path)
                idx += 1

        # Borrar etiquetas del excel
        lbl = [None]*idx
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='traintags', header=False, index=False, startcol=self.nmodel, startrow=1)

        # Borrar TEST
        idx = 0
        filelist = os.listdir(self.dirtest)
        for file in filelist:
            if file.startswith('z_'):
                path = os.path.join(self.dirtest, file)
                os.remove(path)
                idx += 1

        # Borrar etiquetas del excel
        lbl = [None]*idx
        df = pd.DataFrame(list(zip(lbl)))
        with pd.ExcelWriter(self.dirxlsx, mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name='testtags', header=False, index=False, startcol=self.nmodel, startrow=1)



