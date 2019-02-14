from .State import State
import os, json

class CopyState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self)

    def echo(self):
        print(" Print method of CopyState has been called")

    @staticmethod
    def getJobId():
        return State.jobId

    def DoJob(self):
        print("DoJob method of CopyState has been called")
        os.system("robocopy input\ output\ incoming.json")
        with open('input/incoming.json', 'r') as json_file:
            incoming = json.load(json_file)
        # incoming['String To Be Deleted'] = ""

        # Set New Timestamp
        timeStamp =  int(incoming['TimeStamp'])
        timeStamp = timeStamp + 2
        incoming['TimeStamp'] = timeStamp

        # Set New String
        
        with open('output/incoming.json', 'w') as jsonFile:
            json.dump(incoming, jsonFile)
        os.system("robocopy output\ input\ incoming.json")