### Constructor Overriding ###

class Parent:

    def __init__(self):
        print("In constructor")

    def parentFunc(self):
        print("In parent Function")

class Child(Parent):

    def __init__(self):
        print("In child constructor")

obj1 = Child()
obj1.parentFunc()


