// ================================================================================
// Dependencias | librerías
// ================================================================================ 
#include <tinycbor.h> // ***NO MODIFICAR***
// Puede agregar sus librerías a partir de este punto
#include "BluetoothSerial.h"

// ================================================================================
// Funcionamiento básico del robot, ***NO MODIFICAR***
// ================================================================================
uint8_t uart_send_buffer[32] = {0}; // buffer CBOR
static const unsigned int control_time_ms = 100; // período de muestreo del control
volatile float phi_ell = 0; // en rpm
volatile float phi_r = 0; // en rpm

int cont = 0;
int flag = 0;
double speedwheel = 0.0;
BluetoothSerial BT;

void
encode_send_wheel_speeds_task(void * p_params)
{
  TickType_t last_control_time;
  const TickType_t control_freq_ticks = pdMS_TO_TICKS(control_time_ms);

  // Tiempo actual
  last_control_time = xTaskGetTickCount();

  while(1)
  {
    // Se espera a que se cumpla el período de muestreo
    vTaskDelayUntil(&last_control_time, control_freq_ticks);
    
    TinyCBOR.Encoder.init(uart_send_buffer, sizeof(uart_send_buffer));
    TinyCBOR.Encoder.create_array(2);
    TinyCBOR.Encoder.encode_float(phi_ell);
    TinyCBOR.Encoder.encode_float(phi_r);
    TinyCBOR.Encoder.close_container();
    Serial2.write(TinyCBOR.Encoder.get_buffer(), TinyCBOR.Encoder.get_buffer_size());        
  }
}
// ================================================================================


// ================================================================================
// Programar la funcionalidad de visual servoing aquí
// ================================================================================ 
void
visual_servoing_task(void * p_params)
{

  while(1) // loop()
  {
      if (BT.available()) { 
    String datos = BT.readStringUntil('/'); 
    int predict = datos.substring(0, datos.indexOf(',')).toInt(); 
    double lipdif = datos.substring(datos.indexOf(',') + 1).toDouble(); 


    if (lipdif < 0.03) {
      // CÓDIGO !STOP
    
      if (predict == 0) {
                        if (speedwheel != 0.0){
                            phi_ell = (0.60 * speedwheel * 100)
                            phi_r = (speedwheel * 100)
                        }
                        else (){
                            phi_ell = (speedwheel * 100)
                            phi_r = (0.3 * 100)
                        }
      }
      
      else if (predict == 1){
                            phi_ell = (speedwheel * 100)
                            phi_r = (speedwheel * 100)
                            flag = 0
      }
      
      else if (predict == 2){
                        if (speedwheel != 0.0){
                            phi_ell = (speedwheel * 100)
                            phi_r = (0.60 * speedwheel * 100)
                        }
                        else (){
                            phi_ell = (0.3 * 100)
                            phi_r = (speedwheel * 100)
                        }         
      }
      else if (predict == 3){
          // CÓDIGO PARA INCREMENTAR
      }
      else if (predict == 4){
          // CÓDIGO PARA DECREMENTAR
      }
    }

    else if (lipdif >= 0.03){
      // CÓDIGO STOP
  }
 }
    phi_ell = 100;
    phi_r = -100;

    vTaskDelay(1000 / portTICK_PERIOD_MS); // delay de 1 segundo (thread safe)  
  }
}


void 
setup() 
{
  BT.begin("ESP32_UVG");
  Serial.begin(115200); // ***NO MODIFICAR***
  Serial2.begin(115200); // ***NO MODIFICAR***
  TinyCBOR.init(); // ***NO MODIFICAR***

  // Si alguna de sus librerías requiere setup, colocarlo aquí

  // Creación de tasks ***NO MODIFICAR***
  xTaskCreate(encode_send_wheel_speeds_task, "encode_send_wheel_speeds_task", 1024*2, NULL, configMAX_PRIORITIES, NULL);
  xTaskCreate(visual_servoing_task, "visual_servoing_task", 1024*2, NULL, configMAX_PRIORITIES-1, NULL);
}


void 
loop() 
{

}
