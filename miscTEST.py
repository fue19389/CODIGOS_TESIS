import os
import cv2
import math as mt
import numpy as np






# pre-proces para guardar fotos
dirphoto = r'C:\Users\gerar\PycharmProjects\TRAINFACE'
dir = r'C:\Users\gerar\PycharmProjects\PFOTOS'

usrpho = 0
usrlist = os.listdir(dirphoto)
for filename in usrlist:
    if filename.startswith('z'):
        usrpho += 1
grpqtty = int(mt.floor((usrpho / 9) + 1))

pfxname = 'z'
grpname = str(grpqtty)
sfxname = '02.jpg'
jnt = pfxname + grpname + sfxname
savedir = os.path.join(dir, jnt)

# proceso para guardar labels
dirvrbls = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\y_train.npy'
val = 2
y_ttrain = np.load(dirvrbls)
y_t = np.append(y_ttrain, val)



# proceso para capturar y guardar foto

captura = input('ingrese el 1 :')
captura = int(captura)
if captura == 1:
    # set camera
    cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
    _, frame = cap.read()  # return a single frame in variable `frame`

    while captura == 1:
        cv2.imshow('img1', frame)  # display the captured image
        if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
            cv2.imwrite(savedir, frame)
            cv2.destroyAllWindows()
            break

    cap.release()

