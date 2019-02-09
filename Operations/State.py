class State:
    # __init__ is known as the constructor
    def __init__(self, flowName):
        self.flowName = flowName
        print("Constuctor of State class has been called")
        print(flowName)

    def echo(self):
        print(" Print method of Base CLass SHOULD NOT be called")

