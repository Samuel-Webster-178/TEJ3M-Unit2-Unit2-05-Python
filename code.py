# Created by: Samuel Webster
# Created on: June 2023
#
# Rotates a servo motor for 180 degrees, then 180 in the opposite direction.


"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
   for angle in range(0, 180, 5):
       my_servo.angle = angle
       time.sleep(0.05)
   for angle in range(180, 0, -5):
       my_servo.angle = angle
       time.sleep(0.05)
