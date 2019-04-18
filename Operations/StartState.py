from .State import State
import os

class StartState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self)

    def echo(self):
        print(" Print method of StartState has been called")

    @staticmethod
    def setJobId(jid):
        State.jobId = jid

    @staticmethod
    def getJobId():
        return State.jobId

    def DoJob(self):
        print("DoJob method of StartState has been called")
        os.system("cp resources/incoming.json input/incoming.json")
