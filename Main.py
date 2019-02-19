import Operations, json, time, threading, glob, os
from Client import Client

def CleanUpEnvironment():
    files_input = glob.glob('input/*')
    files_output = glob.glob('output/*')
    files_dumps =  glob.glob('dumps/*')
    files_results = glob.glob('results/*')
    for f in files_input:
        os.remove(f)
    for f in files_output:
        os.remove(f)
    for f in files_dumps:
        os.remove(f)
    # for f in files_results:
    #    os.remove(f)

def main():
    # Clean Up Environment First #
    CleanUpEnvironment()

    with open('resources/incoming.json') as json_file:
        incomingFile = json.load(json_file)
    currentFlow = incomingFile['Flow Name']
    jobId = incomingFile['Job Id']
    # StringToBeAdded = incomingFile['String To Be Deleted']

    firstClient = Client(currentFlow, jobId)
    firstClient.startStateMachine()

    secondClient = Client(currentFlow, jobId)
    secondClient.startStateMachine()

    # Clean Up Environment In The End #
    CleanUpEnvironment()


main()


