from controller import Robot, Motor
import tensorflow as tf
import numpy as np
import cv2

TIME_STEP = 32
MAX_SPEED = 6.28
CAP = cv2.VideoCapture(0)
ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or8.keras'
ho_model = tf.keras.models.load_model(ho_model)

# create the Robot instance.
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))


while True:
   _, img = CAP.read()
   imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   imgRGB = cv2.resize(imgRGB, (320, 180))
   imgRGB = imgRGB.astype(int) / 255

   y_predicted = ho_model.predict(np.array([imgRGB]), verbose=None)
   prediction = int(np.argmax(y_predicted))

   if prediction == 0:
      leftMotor.setVelocity(0.25 * MAX_SPEED)
      rightMotor.setVelocity(0.45 * MAX_SPEED)
      robot.stepBegin(TIME_STEP)
   if prediction == 1:
      leftMotor.setVelocity(0.0 * MAX_SPEED)
      rightMotor.setVelocity(0.0 * MAX_SPEED)
      robot.stepBegin(TIME_STEP)
   if prediction == 2:
      leftMotor.setVelocity(0.45 * MAX_SPEED)
      rightMotor.setVelocity(0.25 * MAX_SPEED)
      robot.stepBegin(TIME_STEP)
   if prediction == 3:
      leftMotor.setVelocity(0.45 * MAX_SPEED)
      rightMotor.setVelocity(0.45 * MAX_SPEED)
      robot.stepBegin(TIME_STEP)

   robot.stepEnd()


