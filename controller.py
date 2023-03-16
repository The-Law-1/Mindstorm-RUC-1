from enum import Enum
from behaviours.states import State
from behaviours.drive_forward import DriveForward
from behaviours.stop import Stop
from behaviours.drive_backward import DriveBackward
from behaviours.turn_right import TurnRight

class Controller():
    def __init__(self, motors, IRSensor, colourSensor, deltaTime):
        self.behaviours = [Stop("Stop"), DriveForward("Drive Forward", motors), DriveBackward("Drive Backward", motors, 1000), TurnRight("Turn Right", motors)]
        self.current_behaviour = None
        self.state = State.STOP
        self.deltaTime = deltaTime

        self.colourSensor = colourSensor
        self.IRSensor = IRSensor


    def run(self):
        while True:
            # if you don't have a current behaviour, get one
            if (self.current_behaviour == None):
                return
            else:
                newState = self.current_behaviour.update(self.colourSensor.color(), self.IRSensor.distance())
                self.setState(newState) # will be ignored if it's already in that state

            # sleep delta time?

    def setState(self, state: State):
        if (self.state != state):
            self.state = state

            self.current_behaviour.on_exit()
            # get the behaviour from the list
            self.current_behaviour = self.behaviours[self.state]
            # call on enter
            self.current_behaviour.on_enter()