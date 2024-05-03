import socket
import tensorflow as tf
import numpy as np
import cv2
import faceLANDMARKS as fL

# MAC address of the ESP32 Bluetooth device
esp32_mac_address = "CC:50:E3:96:CC:50"  # Replace with your ESP32's MAC address
# Create a Bluetooth socket object

CAP = cv2.VideoCapture(0)
ho_model = r'C:\Users\gerar\PycharmProjects\EXPOR_TESIS\head_or12.keras'
ho_model = tf.keras.models.load_model(ho_model)
detector = fL.FaceMeshDetector()
flag = 0


while True:

    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    _, imgF = CAP.read()
    img, nodes = detector.findFaceMesh(imgF)
    nodes = np.array([nodes])
    if nodes.any() != 0:
       y_predicted = ho_model.predict(nodes, verbose=None)
       prediction = int(np.argmax(y_predicted))
    else:
       prediction = 1

    # Connect to the ESP32 using channel 4
    sock.connect((esp32_mac_address, 4))
    # Convert integer to bytes before sending
    data_bytes = prediction.to_bytes(4, byteorder='little')  # Assuming integer is 32 bits (4 bytes)
    # Send the data
    sock.sendall(data_bytes)
