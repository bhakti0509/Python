class Parent:
    x = 10
    y = 20

    @classmethod

    def dispData(cls):
        print(cls.x)
        print(cls.y)

class Child:
    x = 30
    y = 40

    @classmethod
    def dispData(cls):
        print(cls.x)
        print(cls.y)

obj = Child()
obj.dispData()
