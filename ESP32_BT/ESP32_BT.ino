#include <BluetoothSerial.h>

BluetoothSerial SerialBT;
#define FORWARD 12
#define RIGHT 27
#define LEFT 25
#define BACKWARD 32

int time_delay = 1000;
int flag = 0;
int count = 0;

void setup() {
  SerialBT.begin("ESP32_BT"); // Bluetooth device name
  pinMode(FORWARD, OUTPUT);
  pinMode(RIGHT, OUTPUT);
  pinMode(LEFT, OUTPUT);
  pinMode(BACKWARD, OUTPUT);
}


void loop() {
  if (SerialBT.available()) {
    int predictInt = SerialBT.read();

    if (predictInt == 0) {
        digitalWrite(LEFT, HIGH); 
    }
    else if (predictInt == 1){
        digitalWrite(LEFT, LOW); 
        digitalWrite(RIGHT, LOW); 
        flag = 0;
    }
    else if (predictInt == 2){
        digitalWrite(RIGHT, HIGH); 
    }
    else if (predictInt == 3){
        if (flag == 0){
          count = count + 1;
          flag = 1;
        }
    }
    else if (predictInt == 4){
        if (flag == 0){
          count = count - 1;
          flag = 1;
        }
    }
    
    // Adjust count to be within range [-4, 4]
    if (count > 4) {
      count = 4;
    } else if (count < -4) {
      count = -4;
    }
    
    if (count > 0) {
      digitalWrite(FORWARD, HIGH);
      delay(time_delay / count); 
      digitalWrite(FORWARD, LOW);  
      delay(time_delay / count);    
    } else if (count < 0) {
      digitalWrite(BACKWARD, HIGH);
      delay(time_delay / (-count)); 
      digitalWrite(BACKWARD, LOW);  
      delay(time_delay / (-count));         
    } else {
      digitalWrite(FORWARD, LOW); 
      digitalWrite(BACKWARD, LOW);
    }
  }
}
