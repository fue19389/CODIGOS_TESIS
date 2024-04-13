from controller import Robot, Motor
import tensorflow as tf
import numpy as np
import cv2
import faceLANDMARKS as fL

TIME_STEP = 32
MAX_SPEED = 6.28
CAP = cv2.VideoCapture(0)
ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
ho_model = tf.keras.models.load_model(ho_model)

# create the Robot instance.
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
detector = fL.FaceMeshDetector()
cont = 0
SPEEDC = 0
flag = 0


while True:
   _, imgF = CAP.read()
   img, nodes = detector.findFaceMesh(imgF)
   nodes = np.array([nodes])
   if nodes.any() != 0:
      y_predicted = ho_model.predict(nodes, verbose=None)
      prediction = int(np.argmax(y_predicted))
   else:
      prediction = 1


   if prediction == 0:
      if SPEEDC != 0:
         leftMotor.setVelocity(0.70 * SPEEDC * MAX_SPEED)
         rightMotor.setVelocity(SPEEDC * MAX_SPEED)
      else:
         leftMotor.setVelocity(SPEEDC * MAX_SPEED)
         rightMotor.setVelocity(0.3 * MAX_SPEED)
      robot.stepBegin(TIME_STEP)
   if prediction == 1:
      leftMotor.setVelocity(SPEEDC * MAX_SPEED)
      rightMotor.setVelocity(SPEEDC * MAX_SPEED)
      flag = 0
      robot.stepBegin(TIME_STEP)
   if prediction == 2:
      if SPEEDC != 0:
         leftMotor.setVelocity(SPEEDC * MAX_SPEED)
         rightMotor.setVelocity(0.70 * SPEEDC * MAX_SPEED)
      else:
         leftMotor.setVelocity(0.3 * MAX_SPEED)
         rightMotor.setVelocity(SPEEDC * MAX_SPEED)
      robot.stepBegin(TIME_STEP)
       
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
      robot.stepBegin(TIME_STEP)
       
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
      robot.stepBegin(TIME_STEP)

   else:
      pass

   print(prediction, cont, SPEEDC)
   robot.stepEnd()


