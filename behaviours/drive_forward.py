from .base import Behaviour
from .states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT, DRIVE_OBJECT
from pybricks.parameters import Color

class DriveForward(Behaviour):
    def __init__(self, name, motors):
        Behaviour.__init__(self, name)
        self.speed = 300
        self.motors = motors
        self.redObject = False
        self.blueObject = False

    def update(self, detectedColour, detectedProximity):
        global redObject, blueObject

        # if you see black, stop
        for motor in self.motors:
            motor.run_time(self.speed, 1000, wait=False)

        if (detectedColour == Color.BLACK):
            return DRIVE_BACKWARD
            # self.robot.stop()
        # if (self.proximitySensor.distance() < 100):
        #     return State.STOP

        if (detectedColour == Color.RED and self.redObject == False):
            self.redObject = True
            return DRIVE_OBJECT
        if (detectedColour == Color.BLUE and self.blueObject == False):
            self.blueObject = True
            return DRIVE_OBJECT

        return DRIVE_FORWARD

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
