import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
R_LED = 16
G_LED = 18
B_LED = 22

GPIO.setup(R_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B_LED, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(G_LED, GPIO.HIGH)
time.sleep(3)
GPIO.output(G_LED, GPIO.LOW)
GPIO.output(B_LED, GPIO.HIGH)
time.sleep(1)
GPIO.output(B_LED, GPIO.LOW)
GPIO.output(R_LED, GPIO.HIGH)
time.sleep(2)
GPIO.output(R_LED, GPIO.LOW)


try:
	while True:
		key = int(input("press number 1 or 0\n"))
		if key == 1:
			GPIO.output(R_LED, GPIO.HIGH)
			GPIO.output(G_LED, GPIO.HIGH)
			GPIO.output(B_LED, GPIO.HIGH)
		elif key == 0:
			GPIO.output(R_LED, GPIO.LOW)
			GPIO.output(G_LED, GPIO.LOW)
			GPIO.output(B_LED, GPIO.LOW)
finally:
	GPIO.cleanup()
	
			
		

