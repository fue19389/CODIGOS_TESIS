import os
import cv2
import math as mt


dir = r'C:\Users\gerar\PycharmProjects\PFOTOS'
dirphoto = r'C:\Users\gerar\PycharmProjects\TRAINFACE'

i = 0
usrlist = os.listdir(dirphoto)
for filename in usrlist:
    if filename.startswith('z'):
        i += 1

grpqtty = int(mt.floor((i / 9) + 1))

pfxname = 'z'
grpname = str(grpqtty)
sfxname = '02.jpg'
tuple = (pfxname, grpname, sfxname)
jnt = ''.join(tuple)
savedir = os.path.join(dir, jnt)




cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
_, frame = cap.read()  # return a single frame in variable `frame`




while (True):
    cv2.imshow('img1', frame)  # display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
        cv2.imwrite(savedir, frame)
        cv2.destroyAllWindows()
        break

cap.release()

