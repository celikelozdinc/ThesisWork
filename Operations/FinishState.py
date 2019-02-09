from .State import State
import os

class FinishState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self)

    def echo(self):
        print(" Print method of FinishState has been called")


    @staticmethod
    def getJobId():
        return State.jobId

    def DoJob(self):
        print("DoJob method of FinishState has been called")
        os.system("robocopy input\ output\ incoming.json")
