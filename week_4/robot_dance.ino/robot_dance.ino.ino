#include <Servo.h>
Servo servoRight;
Servo servoLeft;


void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(11);
}
void stop_that_robot(){
 
  servoLeft.writeMicroseconds(1500);
  //delay(1000);
  servoRight.writeMicroseconds(1500);
  //delay(1000);
}
void forwards(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}
void backwards(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}
void left(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  
}
void right(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
}
void loop() {
  // put your main code here, to run repeatedly:
  forwards();
  delay(200);
  stop_that_robot();
  delay(200);
  backwards();
  delay(200);
  stop_that_robot();
  delay(200);
  forwards();
  delay(200);
  stop_that_robot();
  delay(200);
  backwards();
  delay(200);
  stop_that_robot();
  delay(200);
  left();
  delay(200);
  left();
  delay(200);
  left();
  //forwards();
  delay(200);
  left();
  //forwards();
  delay(200);
  left();
  //forwards();
  delay(200);
  left();
  //forwards();
  delay(200);
  left();
  delay(200);
  left();
  delay(200);
  left();
  delay(200);
  left();
  delay(200);
  left();
  delay(200);
  left();
  forwards();
  delay(200);
  stop_that_robot();
  delay(200);
  backwards();
  delay(200);
  stop_that_robot();
  delay(200);
  left();
  //forwards();
  delay(550);
  forwards();
  delay(300);
  stop_that_robot();
  delay(200);
  backwards();
  delay(200);
  stop_that_robot();
  delay(200);
  right();
//  //forwards();
//  delay(1000);
//  forwards();
//  delay(200);
//  stop_that_robot();
//  delay(200);
//  backwards();
//  delay(200);
//  stop_that_robot();
//  delay(200);
//  stop_that_robot();
//  delay(1000);
//  backwards();
//  delay(1000);
//  stop_that_robot();
}

