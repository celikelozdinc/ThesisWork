from .State import State
import os, datetime

class FinishState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self)

    def echo(self):
        print(" Print method of FinishState has been called")

    @staticmethod
    def getJobId():
        return State.jobId

    @staticmethod
    def getCurrentTimeStamp():
        return State.currentTimeStamp


    def DoJob(self):
        print("DoJob method of FinishState has been called")
        os.system("robocopy output\ results\ incoming.json")

        os.rename('results\incoming.json', 'results\outgoing.json')

        timeStampString = FinishState.getCurrentTimeStamp()
        curTS = datetime.datetime.strptime(timeStampString, '%a, %d %b %Y %H:%M:%S GMT')
        newFile = "results\outgoing@"+ str(curTS.hour) + "." + str(curTS.minute) + "." + str(curTS.second) + '.json'
        os.rename('results\outgoing.json',newFile)

        os.system("robocopy dumps\ results\ ")
        print("Finished: TimeStamp is: ", FinishState.getCurrentTimeStamp())
