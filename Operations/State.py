class State:
    # static variable
    jobId = -1

    # __init__ is known as the constructor
    def __init__(self):
        print("Constuctor of State class has been called")

    def echo(self):
        print("Print method of Base Class SHOULD NOT be called")

    def DoJob(self):
        print("DoJob method of Base Class SHOULD NOT be called")
