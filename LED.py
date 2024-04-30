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
