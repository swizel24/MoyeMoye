int LED1 = 1;
int LED2 = 2;
int LED3 = 3;
int LED4 = 4;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED1, HIGH);
  delay(200);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH);
  delay(200);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, HIGH);
  delay(200);
  digitalWrite(LED3, LOW);
  digitalWrite(LED4, HIGH);
  delay(200);
  digitalWrite(LED4, LOW);
  digitalWrite(LED3, HIGH);
  delay(200);
  digitalWrite(LED3, LOW);
  digitalWrite(LED2, HIGH);
  delay(200);
  digitalWrite(LED2, LOW);
}


servo
#include <Servo.h>
Servo myservo;
int servoPin=3;

void setup(){
  myservo.attach(servoPin);
}

void loop(){
  for (int i=0; i<=180; i+=20)
  {
  myservo.write(i);
  delay(500);
}
delay(1000);

for (int i=180; i>=0; i-=20)
{
  myservo.write(i);
  delay(500);
  }
  delay(1000);
}



int pirPin=2;
int ledpin=13;

void setup(){
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pinMode(ledpin, OUTPUT);
}



  void loop(){
  int pirstate= digitalRead(pirPin);
  if (pirstate==HIGH)
  {
    Serial.println("motion detected");
    digitalWrite(ledpin, HIGH);
    delay(20);
  }
  else{
    Serial.println("motion not detected");
    digitalWrite(ledpin, LOW);
  }
}





import Adafruit_DHT;
gpio=17 #connect to pin number 11
sensor=Adafruit_DHT.DHT11;

humidity,temperature=Adafruit_DHT.read_retry(sensor,gpio)
if temperature is not None and humidity is not None:
	print("Temp={0:0.1f}*c Humdity={1:0.1f}%".format(temperature,humidity))
else:
	print("failed to get reading .Try again")
#VCC Pin:(5v:P:2,4)(3v:1,17)
#Ground Pin: (6,9,14,20,25,30,34,39)
#GPIO2:3
#GPIO3:5
#gpio4:7
#gpio14:8
#gpio15:10
#gpio17:11



import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
	GPIO.output(11,True)
	print("LED on")
	time.sleep(1)
	GPIO.output(11,False)
	print("LED off")
	time.sleep(1)
