#include "BluetoothSerial.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_BT"); // Bluetooth device name
}

void loop() {
  if (SerialBT.available()) {
    int receivedInt = SerialBT.read(); // Read the incoming byte as an integer
    Serial.print("Received: ");
    Serial.println(receivedInt);
  }
}
