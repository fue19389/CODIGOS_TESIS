from controller import self.robot, Motor
import tensorflow as tf
import numpy as np
import cv2
import subprocess
import faceLANDMARKS as fL


class wModel:
    def __init__(self):
      
        self.TIME_STEP = 32
        self.MAX_SPEED = 6.28
        self.CAP = cv2.VideoCapture(0)
        self.ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
        self.ho_model = tf.keras.models.load_model(self.ho_model)
        self.webots_path = r'C:\Program Files\Webots\msys64\mingw64\bin\webotsw.exe'
        self.webots_world = r'C:\Users\gerar\PycharmProjects\CODIGOS_TESIS\ho_sim\worlds\ho_sim.wbt'
        self.open_com = [self.webots_path, "--mode=fast", self.webots_world]
        subprocess.Popen(self.open_com)

        # create the self.robot instance.
        self.robot = self.robot()

        # get a handler to the motors and set target position to infinity (speed control)
        self.leftMotor = self.robot.getDevice('left wheel motor')
        self.rightMotor = self.robot.getDevice('right wheel motor')
        self.leftMotor.setPosition(float('inf'))
        self.rightMotor.setPosition(float('inf'))
        self.detector = fL.FaceMeshDetector()





    def on(self):
        cont = 0
        SPEEDC = 0
        flag = 0
        while True:
            _, imgF = self.CAP.read()
            img, nodes = self.detector.findFaceMesh(imgF)
            nodes = np.array([nodes])
            if nodes.any() != 0:
                y_predicted = self.ho_model.predict(nodes, verbose=None)
                prediction = int(np.argmax(y_predicted))
            else:
                prediction = 1


            if prediction == 0:
                if SPEEDC != 0:
                    self.leftMotor.setVelocity(0.70 * SPEEDC * self.MAX_SPEED)
                    self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                else:
                    self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                    self.rightMotor.setVelocity(0.3 * self.MAX_SPEED)
                self.robot.stepBegin(self.TIME_STEP)
            if prediction == 1:
                self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                flag = 0
                self.robot.stepBegin(self.TIME_STEP)
            if prediction == 2:
                if SPEEDC != 0:
                    self.leftMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                    self.rightMotor.setVelocity(0.70 * SPEEDC * self.MAX_SPEED)
                else:
                    self.leftMotor.setVelocity(0.3 * self.MAX_SPEED)
                    self.rightMotor.setVelocity(SPEEDC * self.MAX_SPEED)
                self.robot.stepBegin(self.TIME_STEP)

            if prediction == 3:
                if flag == 0:
                    cont += 1
                if cont > -5 and cont < 5:
                    SPEEDC = cont/4
                if cont > 4:
                    cont = 4
                    SPEEDC = cont/4
                if cont < -4:
                    cont = -4
                    SPEEDC = cont/4
                flag = 1
                else:
                    pass
            self.robot.stepBegin(self.TIME_STEP)

            if prediction == 4:
                if flag == 0:
                    cont -= 1
                if cont > -5 and cont < 5:
                    SPEEDC = cont/4
                if cont > 4:
                    cont = 4
                    SPEEDC = cont/4
                if cont < -4:
                    cont = -4
                    SPEEDC = cont/4
                flag = 1
            else:
                pass
            self.robot.stepBegin(self.TIME_STEP)

            else:
                pass

            print(self.prediction, cont, SPEEDC)
            self.robot.stepEnd()

    def stop(self):
        self.CAP.release()
        cv2.destroyAllWindows()
