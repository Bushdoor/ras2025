import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 12

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

PWM_led = GPIO.PWM(LED, 500)

PWM_led.start(0)

try:
	while True:
		for val in range(0, 100, 10):
			PWM_led.ChangeDutyCycle(val)
			time.sleep(0.5)
		for val in range(100, 0, -10):
			PWM_led.ChangeDutyCycle(val)
			time.sleep(0.5)
			
		
except KeyboardInterrupt:
	pass
	
finally:
	PWM_led.stop()
	GPIO.cleanup()
