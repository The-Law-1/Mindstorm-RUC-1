from base import Behaviour
from states import State
from pybricks.parameters import Color

class TurnRight(Behaviour):
    def __init__(self, name, motors):
        Behaviour.__init__(self, name)
        self.currentangle = 500 # randomize between 45-135?
        self.speed = 500
        self.motors = motors
        self.doneTurn = False

    def update(self, detectedColour, detectedProximity) -> State:

        # when both motors are stopped, return to drive forward
        if (self.motors[0].speed == 0 and self.motors[1].speed == 0):
            return State.DRIVE_FORWARD

        return State.TURN_RIGHT

    def on_enter(self):
        # start running motor[0] at 500 degrees per second
        self.motors[0].run_target(self.speed, self.currentangle, wait=False)
        self.motors[1].run_target(-self.speed, self.currentangle, wait=False)

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
