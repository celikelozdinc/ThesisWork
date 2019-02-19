import Operations, json, time, threading, glob, os

def CleanUpEnvironment():
    files_input = glob.glob('input/*')
    files_output = glob.glob('output/*')
    files_dumps =  glob.glob('dumps/*')
    for f in files_input:
        os.remove(f)
    for f in files_output:
        os.remove(f)
    for f in files_dumps:
        os.remove(f)

def CopyThread(copyState):
    print("Starting Copy Thread")
    copyState.DoJob()
    time.sleep(1.1)
    print("Exiting Copy Thread")

def DumpThread(copyState):
    print("Starting Dump Thread")
    copyState.DoDump()
    time.sleep(2.2)
    print("Exiting Dump Thread")

def OperationFlow(flow, jobId):
    if flow == "COPY":
        print(flow)
        startState = Operations.StartState.StartState()
        copyState = Operations.CopyState.CopyState()
        finishState = Operations.FinishState.FinishState()
        # startState.echo()
        # finishState.echo()
        startState.setJobId(jobId)
        print(finishState.getJobId())

        # Create two threads #
        delay = 60 * 0.5  # for 0.5 minute delay
        close_time = time.time() + delay
        startState.DoJob()

        while True:
            if time.time() > close_time:
                break
            threading.Thread(name='CopyThread', target=CopyThread(copyState)).start()
            threading.Thread(name='DumpThread', target=DumpThread(copyState)).start()

        finishState.DoJob()
        #                    #


    else:
        print(flow)


def main():
    # Clean Up Environment First #
    CleanUpEnvironment()

    with open('resources/incoming.json') as json_file:
        incomingFile = json.load(json_file)
    currentFlow = incomingFile['Flow Name']
    jobId = incomingFile['Job Id']
    # StringToBeAdded = incomingFile['String To Be Deleted']
    OperationFlow(currentFlow, jobId)


    # Clean Up Environment In The End #
    CleanUpEnvironment()


main()


