import behaviours.states as State
from behaviours.drive_forward import DriveForward
from behaviours.stop import Stop
from behaviours.drive_backward import DriveBackward
from behaviours.turn_right import TurnRight
from behaviours.turn_left import TurnLeft
from behaviours.states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT

class Controller():
    def __init__(self, ev3, motors, IRSensor, colourSensor, deltaTime):
        self.behaviours = [DriveForward("Drive Forward", motors), DriveBackward("Drive Backward", motors, 1000), TurnLeft("Turn Left", motors), TurnRight("Turn Right", motors), Stop("Stop")]
        self.state = -1
        self.current_behaviour = None
        self.deltaTime = deltaTime

        self.colourSensor = colourSensor
        self.IRSensor = IRSensor

        self.ev3 = ev3

    def run(self):
        while True:
            # print detected colour
            # if you don't have a current behaviour, get one
            if (self.current_behaviour == None):
                self.setState(DRIVE_FORWARD)
                continue
            else:
                newState = self.current_behaviour.update(self.colourSensor.color(), self.IRSensor.distance())
                self.setState(newState) # will be ignored if it's already in that state

            # sleep delta time?

    def setState(self, state):
        if (self.state != state):
            self.state = state

            if (self.current_behaviour != None):
                self.current_behaviour.on_exit()

            # get the behaviour from the list
            self.current_behaviour = self.behaviours[self.state]

            self.ev3.speaker.say(self.current_behaviour.name)

            # call on enter
            self.current_behaviour.on_enter()