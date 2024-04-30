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

