"""Rough draft of VPD controller, pass in arguments for veg or flower"""
import board
import busio
import digitalio
import adafruit_bme280
import math
import RPi.GPIO as GPIO  
import time 
import sys

mode = sys.argv[1]
bme280 = adafruit_bme280.Adafruit_BME280_SPI(busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO), digitalio.DigitalInOut(board.D5))
#GPIO.setmode(GPIO.BCM)
#GPIO.setup("""ENTER CHANNEL HERE for humidifier relay""", GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup("""ENTER CHANNEL HERE for dehumidifier relay""", GPIO.OUT, initial=GPIO.HIGH)
avg_vpd = []
def dewpoint():
	"""Calculates the dewpoint"""
	b = 17.368
	c = 238.88
	gamma = (b * bme280.temperature /(c + bme280.temperature)) + math.log(bme280.humidity / 100.0)
	return (c * gamma) / (b - gamma)
def vpd():
	"""You down with VPD?  Yeah, you know me.....
	Ideals:
		veg    = .9 to 1.1
		flower = 1.2 to 1.5
	"""
	svp = (610.78 * math.e**(bme280.temperature/(bme280.temperature + 238.3) * 17.2694))/1000
	return svp * (1-bme280.humidity/100)
def qnd_log():
	"""Quick and dirty logger, mainly to track average VPD values during light hours.  I have a SensorPush which I'm happy with to do pretty logging for Temp and Humidity.  You can add better functionality through thingspeak or my recommendation would be adding an apache webserver, a sql db and nice graphing.  Then you could view it remotely once you setup port forwarding on your router."""
	global avg_vpd
	path = '/home/neal/log.txt'
	avg_vpd.append(vpd())
	if len(avg_vpd) > 100:
		f = open(path,'a')
		f.write('Average VPD during light hours over the last 100 samples is {} at {}'.format((sum(avg_vpd)/len(avg_vpd)),time.ctime(time.time())))
		f.write('\n')
		f.close()
		avg_vpd = []

try:
	while True:
		print("\nTemperature: {:0.1f} °C".format(bme280.temperature))
		print("Humidity: {:0.1f} %".format(bme280.humidity))
		print("VPD: {:0.2f} ".format(vpd()))
		print("Dewpoint: {:0.2f} °C".format(dewpoint()))
		if time.localtime(time.time()).tm_hour >= 3 and time.localtime(time.time()).tm_hour <= 20 and mode == 'veg':
			qnd_log()
		elif time.localtime(time.time()).tm_hour >= 7 and time.localtime(time.time()).tm_hour <= 18 and mode == 'flower':
			qnd_log()
		time.sleep(60)
		#if time.localtime(time.time()).tm_hour >= 3 and time.localtime(time.time()).tm_hour <= 20 and vpd() < 0.9 and mode == 'veg':
			#"""Too steamy brah, reduce that shit"""
			#while vpd() < 1.1:
			#	GPIO.output("""ENTER CHANNEL HERE for dehumidifier""", GPIO.LOW)
			#	print("Reducing humidity, VPD should be between 0.9 and 1.1.  VPD is currently at {}".format(vpd()))
			#	time.sleep(30)
			#GPIO.output("""ENTER CHANNEL HERE for dehumidifier""", GPIO.HIGH)
			#time.sleep(30)
		#elif time.localtime(time.time()).tm_hour >= 3 and time.localtime(time.time()).tm_hour <= 20 and vpd() > 1.1 and mode == 'veg':
			#"""Humidify that bitch, nozzle in middle"""
			#while vpd() > 0.9:
			#	GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.LOW)
			#	print("Increasing humidity, VPD should be between 0.9 and 1.1.  VPD is currently at {}".format(vpd()))
			#	time.sleep(30)
			#GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.HIGH)
			#time.sleep(30)
		#elif time.localtime(time.time()).tm_hour >= 7 and time.localtime(time.time()).tm_hour <= 18 and vpd() < 1.2 and mode == 'flower':
			#"""Too steamy brah, reduce that shit"""
			#while vpd() < 1.5:
			#	GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.LOW)
			#	print("Reducing humidity, VPD should be between 1.2 and 1.5.  VPD is currently at {}".format(vpd()))
			#	time.sleep(30)
			#GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.HIGH)
		#elif time.localtime(time.time()).tm_hour >= 7 and time.localtime(time.time()).tm_hour <= 18 and vpd() > 1.5 and mode == 'flower' and bme280.temperature < 30:
			#"""Humidify that bitch, nozzle in middle"""
			#while vpd() < 1.2:
			#	GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.LOW)
			#	print("Increasing humidity, VPD should be between 1.2 and 1.5.  VPD is currently at {}".format(vpd()))
			#	time.sleep(30)
			#GPIO.output("""ENTER CHANNEL HERE for humidifier""", GPIO.HIGH)
except KeyboardInterrupt:
	GPIO.cleanup()