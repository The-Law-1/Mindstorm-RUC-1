from base import Behaviour
from states import State
from pybricks.parameters import Color

class DriveForward(Behaviour):
    def __init__(self, name, motors):
        Behaviour.__init__(self, name)
        self.speed = 500
        self.motors = motors

    def update(self, detectedColour, detectedProximity) -> State:
        # if you see black, stop
        if (detectedColour == Color.BLACK):
            return State.STOP
            # self.robot.stop()
        # if (self.proximitySensor.distance() < 100):
        #     return State.STOP
        return State.DRIVE_FORWARD

    def on_enter(self):
        # start the robot
        for motor in self.run():
            motor.run(self.speed, wait=False)

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
