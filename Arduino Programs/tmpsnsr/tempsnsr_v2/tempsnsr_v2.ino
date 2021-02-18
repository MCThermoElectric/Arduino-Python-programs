#include <DallasTemperature.h>
#include <DS18B20.h>
// in the final version of the code, i plan to use an array to store all the different sensor lines we will be using.
// I will loop thru the array to access the different lines of sensors.
// each individual line takes a single digital pin and can hold an unlimited number of sensors.
// However, I believe that each additional sensor on a line will slow the measuring speed down (just a theory, not necessarily true)

DS18B20 tempSensor(2);


void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(2, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int i = 1;
  while(tempSensor.selectNext()) {
    //Serial.print(String(i) + "&");
    Serial.print(String(tempSensor.getTempC()) + ",");
    i++;
  }
  Serial.println();
  
}
