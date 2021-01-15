#include <DallasTemperature.h>
#include <DS18B20.h>

DS18B20 tempSensor(2);


void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  int i = 1;
  while(tempSensor.selectNext()) {
    Serial.println("Sensor #" + String(i) + ": " + tempSensor.getTempF() + " °F");
    i++;
  }

}
