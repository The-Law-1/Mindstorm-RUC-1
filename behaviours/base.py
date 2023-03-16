from states import State

class Behaviour:
    def __init__(self, name, ):
        self.name = name

    def update(self, detectedColour, detectedProximity) -> State:
        print(self.name + "update loop")

    def on_enter(self):
        print(self.name + "on enter")

    def on_exit(self):
        print(self.name + "on exit")
