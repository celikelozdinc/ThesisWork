import Operations
import json
# import time


def OperationFlow(flow):
    if flow == "INSTALL":
        print(flow)
        startState = Operations.StartState.StartState()
        startState.echo()
        finishState = Operations.FinishState.FinishState()
        finishState.echo()

    else:
        print(flow)


def main():
    with open('resources/incoming.json') as json_file:
        incomingFile = json.load(json_file)
        currentFlow = incomingFile['Flow Name']
        # print(currentFlow)
        OperationFlow(currentFlow)



main()


