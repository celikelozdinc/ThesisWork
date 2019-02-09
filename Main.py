import Operations
import json
# import time


def OperationFlow(flow, jobId, StringToBeAdded):
    if flow == "COPY":
        print(flow)
        startState = Operations.StartState.StartState()
        finishState = Operations.FinishState.FinishState()
        # startState.echo()
        # finishState.echo()
        startState.setJobId(jobId)
        print(finishState.getJobId())
        startState.DoJob()
        finishState.DoJob()


    else:
        print(flow)


def main():
    with open('resources/incoming.json') as json_file:
        incomingFile = json.load(json_file)
    currentFlow = incomingFile['Flow Name']
    jobId = incomingFile['Job Id']
    StringToBeAdded = incomingFile['String To Be Deleted']
    OperationFlow(currentFlow, jobId, StringToBeAdded)



main()


