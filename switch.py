import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

R_LED = 16
G_LED = 18
B_LED = 22
switch= 10

GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B_LED, GPIO.OUT, initial=GPIO.LOW)

flag= False

while True:
	if GPIO.input(switch) == GPIO.HIGH:
			flag = not flag
			GPIO.output(R_LED, flag)
			GPIO.output(G_LED, flag)
			GPIO.output(B_LED, flag)
			print("LED ON")
			time.sleep(0.3)
