from base import Behaviour
from states import State

class Stop(Behaviour):
    def __init__(self, name):
        Behaviour.__init__(self, name)
        self.speed = 500

    def update(self, detectedColour, detectedProximity) -> State:
        return State.STOP