import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pylab as plt
import math
from glob import glob


class FaceMeshDetector:

    def __init__(self, staticMode=False, maxFaces=1, refineLm=False, minDetectionCon=0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.refineLm = refineLm
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        # Utilization of libraries for mesh and drawing of mediapipe
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
                                                 self.refineLm, self.minDetectionCon,
                                                 self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))

    def findFaceMesh(self, img, draw=True):

        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)

        # Ciclo para dibujar los landmarks, si es que se detecta una cara

        nodes = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)

                # Ciclo para obtener los landmarks en pixels y originales
                npoints = []
                for id, lm in enumerate(faceLms.landmark):
                    # if id % 2 == 0: # Here we have the visual identification of multiples of 5 landmarks
                    # if id == 467:
                    ih, iw, ic = img.shape
                    npoints.append([lm.x, -1*(lm.y)+1])

                nodes.append(npoints)
                nodes = np.squeeze(np.array(nodes))

        return img, nodes


def main():
    # Capture photo

    cap = cv2.VideoCapture(0)

    # Variables
    detector = FaceMeshDetector()

    while True:
        # Saving captured image and transforming from BGR TO RGB
        success, imgF = cap.read()
        # imgF = cv2.imread(r'C:\Users\gerar\PycharmProjects\COMPLETEDATABASE\TRAIN\z_00_73.jpg') #SPECIAL ONE
        # imgF = cv2.imread(r'C:\Users\gerar\PycharmProjects\COMPLETEDATABASE\TRAIN\z_01_137.jpg')
        img, nodes = detector.findFaceMesh(imgF)

        cv2.imshow('Image', img)
        key = cv2.waitKey(30)
        if key == 27:  # 27= Esc
            break

    if len(nodes) == 0:
        pass
    else:
        x, y = nodes.T
        plt.scatter(x, y)
        plt.show()
        print(nodes.shape)




if __name__ == '__main__':
    main()

