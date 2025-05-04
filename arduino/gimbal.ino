#include <Servo.h>

Servo panServo;
Servo tiltServo;

int panAngle = 90;   // Start centered
int tiltAngle = 90;

void setup() {
  Serial.begin(9600);
  panServo.attach(9);
  tiltServo.attach(10);
  panServo.write(panAngle);
  tiltServo.write(tiltAngle);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    if (commaIndex != -1) {
      int dx = data.substring(0, commaIndex).toInt();
      int dy = data.substring(commaIndex + 1).toInt();

      // Apply step increments, clamp to [0, 180]
      panAngle = constrain(panAngle + dx * 2, 0, 180);
      tiltAngle = constrain(tiltAngle + dy * 2, 0, 180);

      panServo.write(panAngle);
      tiltServo.write(tiltAngle);
    }
  }
}
