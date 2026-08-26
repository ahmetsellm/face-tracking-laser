#include <Servo.h>

Servo servoX;
Servo servoY;

const int servoXPin = 6;
const int servoYPin = 9;

void setup() {
  Serial.begin(9600);
  
  servoX.attach(servoXPin);
  servoY.attach(servoYPin);

  servoX.write(90);
  servoY.write(90);
  
  Serial.println("Sistem hazir. Python'dan veri bekleniyor...");
}

void loop() {
  if (Serial.available() > 0) {
    
    int angle_x = Serial.parseInt(); 
    int angle_y = Serial.parseInt(); 

    while(Serial.available() > 0 && Serial.read() != '\n');

    angle_x = constrain(angle_x, 0, 180);
    angle_y = constrain(angle_y, 0, 180);

    servoX.write(angle_x);
    servoY.write(angle_y);

    Serial.print("Hareket -> X: ");
    Serial.print(angle_x);
    Serial.print(" | Y: ");
    Serial.println(angle_y);
  }
}
