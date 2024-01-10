

class Parent:
    z = 30

    def __init__(self):
        print("In parent constructor")
        self.x = 10
        self.y = 20

    def dispData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispParent(cls):
        print(cls.z)

    def __del__(self):
        print("In dectructor")

obj1 = Parent()
obj2 = Parent()
del obj1

print("Code ended")

