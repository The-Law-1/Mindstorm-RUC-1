from .base import Behaviour
from .states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT, DRIVE_OBJECT
from pybricks.parameters import Color
import time

class DriveObject(Behaviour):
    def __init__(self, name, motors, ev3):
        Behaviour.__init__(self, name)
        self.speed = 300
        self.motors = motors
        self.ev3 = ev3

    def update(self, detectedColour, detectedProximity):
        # if you see black, stop
        for motor in self.motors:
            motor.run_time(self.speed, 1000, wait=False)

        if (detectedColour == Color.BLACK):
            for motor in self.motors:
                motor.run_time(self.speed, 1000, wait=False)
            time.sleep(1)
            self.ev3.speaker.say("Object Out of the way")
            time.sleep(1)
            for motor in self.motors:
                motor.run_time(-self.speed, 1000, wait=False)
            time.sleep(1)
            return DRIVE_BACKWARD
            # self.robot.stop()
        # if (self.proximitySensor.distance() < 100):
        #     return State.STOP
        return DRIVE_OBJECT

    def on_enter(self):

        # start the robot
        # for motor in self.motors:
        #     motor.run(self.speed)
        return

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
