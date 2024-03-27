import cv2
import mediapipe as mp
import time
import numpy as np
import matplotlib.pylab as plt
import math
from glob import glob


class FaceMeshDetector:

    def __init__(self, staticMode=False, maxFaces=2, refineLm=False, minDetectionCon=0.5, minTrackCon=0.5):

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
        nface = []
        nodes = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)

                # Ciclo para obtener los landmarks en pixels
                fpoints = []
                npoints = []
                for id, lm in enumerate(faceLms.landmark):
                    # if id % 2 == 0: # Here we have the visual identification of multiples of 5 landmarks
                    # if id == 467:
                        ih, iw, ic = img.shape
                        x, y0 = int(lm.x * iw), int(lm.y * ih)
                        y = int(-1*(lm.y*ih)+ih)
                        fpoints.append([x, y])
                        npoints.append([id, lm.x, -1*(lm.y)+1])

                        if draw:
                            # Draw selected landmarks in a differente color (RED)
                            cv2.circle(img, (x, y0), 3, (0, 0, 255), cv2.FILLED)

                nface.append(fpoints)
                nodes.append(npoints)

        return img, nface, nodes


def main():
    # Capture photo

    cap = cv2.VideoCapture(0)

    # Capture webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # HIGH RESOLUTION
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    # # lOW RESOLUTION
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)

    # Variables
    detector = FaceMeshDetector()

    while True:
        # Saving captured image and transforming from BGR TO RGB
        success, img = cap.read()
        img, nface, nodes = detector.findFaceMesh(img, draw=False)

        cv2.imshow('Image', img)
        key = cv2.waitKey(30)
        if key == 27:  # 27= Esc
            break


    nodesarray =  np.squeeze(np.array(nodes))
    print(nodesarray.shape)
    nodesarray = nodesarray[:, 1:]
    nfacearray = np.squeeze(np.array(nface))
    x, y = nodesarray.T

    plt.scatter(x, y)
    plt.show()




if __name__ == '__main__':
    main()

