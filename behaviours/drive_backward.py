from base import Behaviour
from states import State
from pybricks.parameters import Color

class DriveBackward(Behaviour):
    def __init__(self, name, motors, duration):
        Behaviour.__init__(self, name)
        self.speed = 500
        self.motors = motors
        self.duration = duration

    def update(self, detectedColour, detectedProximity) -> State:
    
        # when both motors are at speed 0, turn right or left
        if (self.motors[0].speed() == 0 and self.motors[1].speed() == 0):
            return State.TURN_RIGHT

        return State.DRIVE_BACKWARD

    def on_enter(self):
        # start the robot
        for motor in self.run():
            motor.run_time(-self.speed, self.duration, wait=False)
        

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
