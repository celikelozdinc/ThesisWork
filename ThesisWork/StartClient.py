from Client import Client
import json

with open('resources/incoming.json') as json_file:
    incomingFile = json.load(json_file)
currentFlow = incomingFile['Flow Name']
jobId = incomingFile['Job Id']

firstClient = Client(currentFlow, jobId)
firstClient.startStateMachine()


