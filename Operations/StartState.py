from .State import State


class StartState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self, "Operation Flow")

    def echo(self):
        print(" Print method of Start State has been called")

