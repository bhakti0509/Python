class Parent:
    
    def __init__(self):
        print("In constructor parent")
        
    def parentFunc(self):
        print("In parent function")

class Child(Parent):

    def __init__(self):
        #super().__init__()
        
        Parent.__init__(self)

        #Parent()
        
        print("In constructor child")

    def childFunc(self):
        print("In child function")

obj1 = Child()
print(obj1.parentFunc)
obj1.childFunc()

