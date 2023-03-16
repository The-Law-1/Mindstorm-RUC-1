from .base import Behaviour
from .states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT

class Stop(Behaviour):
    def __init__(self, name):
        Behaviour.__init__(self, name)
        self.speed = 500

    def update(self, detectedColour, detectedProximity):
        return STOP