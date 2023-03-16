from enum import Enum

class State(Enum):
    DRIVE_FORWARD = 0
    DRIVE_BACKWARD = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    STOP = 4