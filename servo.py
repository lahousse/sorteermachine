# set servo angle

# libraries
import RPi.GPIO as GPIO
import time

# set the pin mode and pin number
GPIO.setmode(GPIO.BOARD)
servo_pin = 11

# set the frequency of the PWM signal to control the servo
pwm_freq = 50

# set the duty cycle range to control the servo angle
duty_min = 2.5
duty_max = 12.5

# initialize the GPIO pin for the servo
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, pwm_freq)
pwm.start(0)

# function to set the servo angle
def set_angle(angle):
    duty = (duty_max - duty_min) * angle / 180.0 + duty_min
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)

# cleanup the GPIO pin
pwm.stop()
GPIO.cleanup()
