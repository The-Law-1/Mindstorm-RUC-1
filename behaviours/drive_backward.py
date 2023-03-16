from .base import Behaviour
from .states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT
import time
import random

class DriveBackward(Behaviour):
    def __init__(self, name, motors, duration):
        Behaviour.__init__(self, name)
        self.speed = 500
        self.motors = motors
        self.duration = duration
        self.finished = False

    def update(self, detectedColour, detectedProximity):

        # when both motors are at speed 0, turn right or left
        # if (self.motors[0].speed() == 0 and self.motors[1].speed() == 0):
        #     return TURN_RIGHT

        print("DriveBackward update")
        if (self.finished):
            self.finished = False
            # randomly turn left or right
            if random.randint(0, 1) == 0:
                return TURN_LEFT
            else:
                return TURN_RIGHT

        return DRIVE_BACKWARD

    def on_enter(self):
        # start the robot

        self.motors[0].run_time(-self.speed, self.duration, wait=False)
        self.motors[1].run_time(-self.speed, self.duration, wait=False)

        time.sleep(2)

        print("DriveBackward finished")
        self.finished = True

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
