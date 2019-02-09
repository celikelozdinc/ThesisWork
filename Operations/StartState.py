from .State import State
import os, json

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
        print("DoJob method of FinishState has been called")
        os.system("robocopy resources\ input\ incoming.json")
        with open('input/incoming.json', 'r') as json_file:
            incoming = json.load(json_file)
        incoming['String To Be Deleted'] = ""
        with open('input/incoming.json', 'w') as jsonFile:
            json.dump(incoming, jsonFile)