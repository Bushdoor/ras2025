import RPi.GPIO as GPIO
import time

servo_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)
p.start(0)

try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(12.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(10)
		time.sleep(0.5)
		p.ChangeDutyCycle(7.5)
		time.sleep(0.5)
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		p.ChangeDutyCycle(2.5)
		time.sleep(0.5)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
