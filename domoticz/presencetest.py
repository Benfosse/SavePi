import RPi.GPIO as GPIO
import time
import milight
import os

GPIO.setmode(GPIO.BCM)
capteur = 17
etat = 0
GPIO.setup(capteur, GPIO.IN)
controller = milight.MiLight({'host': '192.168.1.37', 'port': 8899}, wait_duration=0) #Create a controller with 0 wait between commands
light = milight.LightBulb(['rgbw']) #Can specify which types of bulbs to use

print "Demarrage du capteur"
time.sleep(2)
print "Capteur pret a detecte un mouvement"

while True:
   if GPIO.input(capteur):
	if etat == 0:
		controller.send(light.all_off()) # Turn on all lights, equivalent to light.on(0)
		etat = 1
	else:
		controller.send(light.all_on()) # Turn on all lights, equivalent to light.on(0)
		etat = 0
	print "Mouvement detecte"
      	time.sleep(2)
   	time.sleep(2)


