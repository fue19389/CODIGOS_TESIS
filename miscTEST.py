import matplotlib.pylab as plt
from glob import glob
import numpy as np
import cv2

dirVRLBS = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\x_train6.npy'
faces = np.load(dirVRLBS)
face1 = faces[2150]
face1 = face1.astype(np.uint8)
face = cv2.imread(r'C:\Users\gerar\PycharmProjects\PFOTOS\speed.jpeg')
face2 = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
facehsv = cv2.cvtColor(face, cv2.COLOR_BGR2HSV)

skinbottom = np.array([0, 50, 20], np.float32)
skintop = np.array([30, 180, 255], np.float32)

mask1 = cv2.inRange(facehsv, skinbottom, skintop)
# mask11 = cv2.cvtColor(mask1, cv2.COLOR_HSV2RGB)
print(mask1.shape)
cv2.imshow('filtro2', mask1)



blur_kernel = np.array([[0.0625, 0.125, 0.625],
                        [0.125, 0.25, 0.125],
                        [0.0625, 0.125, 0.0625]], np.float32)

sharp_kernel = np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]], )

edge_kernel = np.array([[-1, -1, -1],
                        [-1, 8, -1],
                        [-1, -1, -1]], np.float32)

emboss_kernel = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]], np.float32)

edged = cv2.filter2D(face2, -1, edge_kernel)
sharpened = cv2.filter2D(face2, -1, sharp_kernel)
sharpened = cv2.filter2D(sharpened, -1, edge_kernel)
blurred = cv2.filter2D(face2, -1, blur_kernel)
blurred = cv2.filter2D(blurred, -1, edge_kernel)
embossed = cv2.filter2D(face2, -1, emboss_kernel)
embossed = cv2.filter2D(embossed, -1, edge_kernel)

fig, ax = plt.subplots(3, 2)
ax = ax.reshape(-1)
# ax = ax.reshape(-1)
ax[0].imshow(face2)
ax[1].imshow(edged)
ax[2].imshow(sharpened)
ax[3].imshow(blurred)
ax[4].imshow(embossed)
ax[5].imshow(mask1)
ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')
ax[4].axis('off')
ax[5].axis('off')
ax[0].set_title('original')
ax[1].set_title('bordes')
ax[2].set_title('afilado + bordes')
ax[3].set_title('suavizado + bordes')
ax[4].set_title('realzado + bordes')
ax[5].set_title('filtro de color')

plt.show()
