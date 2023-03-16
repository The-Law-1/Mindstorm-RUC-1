#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import controller as ctrl

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

motor_left = Motor(Port.C)
motor_right = Motor(Port.B)

# Initialize the color sensor.
color_sensor = ColorSensor(Port.S2)
IRSensor = InfraredSensor(Port.S3)

# Write your program here.
# ev3.speaker.beep()

# say hello world
ev3.speaker.say("Start!")

def drive_forward(time=3000):
    motor_left.run_time(500, time, then=Stop.HOLD, wait=False)
    motor_right.run_time(500, time, then=Stop.HOLD, wait=True)

deltaTime = 0.1
controller = ctrl.Controller(ev3, [motor_left, motor_right], IRSensor, color_sensor, deltaTime)

controller.run()


# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
# run the motor for five seconds
# drive_forward(1000)

# ev3.speaker.say("Turning left")

# turn left 90 degrees
# motor_right.run_angle(500, 700, then=Stop.HOLD, wait=True)

# drive_forward(1000)

# ev3.speaker.say("Turning left")

# turn left 90 degrees
# motor_right.run_angle(500, 700, then=Stop.HOLD, wait=True)

# drive_forward(1000)

# ev3.speaker.say("Turning left")
# motor_right.run_angle(500, 700, then=Stop.HOLD, wait=True)

# drive_forward(1000)

# detect colours
# while True:
#     # sensed_color = color_sensor.color()
#     # print(sensed_color)

#     reflection = color_sensor.reflection()
#     print(reflection)



# Play another beep sound.
# ev3.speaker.beep(1000, 500)
