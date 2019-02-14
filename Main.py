import Operations, json, time, glob, os


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

        delay = 60 * 0.5  # for 0.5 minutes delay
        close_time = time.time() + delay
        startState.DoJob()
        while True:
            if time.time() > close_time:
                break
            copyState.DoJob()
            time.sleep(2)
        finishState.DoJob()

    else:
        print(flow)


def main():
    # Clean Up Environment First #
    files_input = glob.glob('input/*')
    files_output = glob.glob('output/*')
    for f in files_input:
        os.remove(f)
    for f in files_output:
        os.remove(f)

    with open('resources/incoming.json') as json_file:
        incomingFile = json.load(json_file)
    currentFlow = incomingFile['Flow Name']
    jobId = incomingFile['Job Id']
    # StringToBeAdded = incomingFile['String To Be Deleted']
    OperationFlow(currentFlow, jobId)


    # Clean Up Environment In The End #
    for f in files_input:
        os.remove(f)
    for f in files_output:
        os.remove(f)


main()


