import
# MAC address of the ESP32 Bluetooth device
esp32_mac_address = "CC:50:E3:96:CC:50"  # Replace this with your ESP32's MAC address

# Establish a Bluetooth connection
sock = pyblue.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((esp32_mac_address, 1))

# Data to be sent
data = 42

# Convert integer to bytes before sending
sock.send(bytes([data]))

# Close the connection
sock.close()