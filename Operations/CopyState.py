from .State import State
import os, json, datetime

class CopyState(State):
    # __init__ is known as the constructor
    def __init__(self):
        State.__init__(self)

    def echo(self):
        print(" Print method of CopyState has been called")

    @staticmethod
    def getJobId():
        return State.jobId

    @staticmethod
    def getCurrentTimeStamp():
        return State.currentTimeStamp

    @staticmethod
    def setCurrentTimeStamp(ts):
        State.currentTimeStamp = ts

    def DoJob(self):
        print("DoJob method of CopyState has been called")
        os.system("cp input/incoming.json output/incoming.json")
        with open('input/incoming.json', 'r') as json_file:
            incoming = json.load(json_file)
        # incoming['String To Be Deleted'] = ""

        # Set New Timestamp #
        ts = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
        # print("Time is ", str(ts))
        # timeStamp =  int(incoming['TimeStamp'])
        # timeStamp = timeStamp + 2
        incoming['TimeStamp'] = str(ts)
        #                   #

        # Set New String #
        #                #

        with open('output/incoming.json', 'w') as jsonFile:
            json.dump(incoming, jsonFile)
        os.system("cp output/incoming.json input/incoming.json")

        # Set Global TimeStamp #
        CopyState.setCurrentTimeStamp(str(ts))
        #                       #

    def DoDump(self):
        timeStampString =  CopyState.getCurrentTimeStamp()
        curTS = datetime.datetime.strptime(timeStampString,'%a, %d %b %Y %H:%M:%S GMT')
        # curTS = datetime.datetime.now()
        print("Dumping the value: ",curTS)
        # with open('output/incoming.json', 'w') as jsonFile:
        #     json.dump(incoming, jsonFile)
        os.system("cp output/incoming.json dumps/incoming.json")
        newFile = 'dumps/dump@' +str(curTS.hour) +"."+str(curTS.minute)+"."+str(curTS.second)  + '.json'
        os.rename('dumps/incoming.json', newFile)
