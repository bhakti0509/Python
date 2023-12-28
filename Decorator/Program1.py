class Demo:
    x = 10
    def __init__(self):
        self.y = 20

    @classmethod
    def disp(cls):
        print(cls.x)

obj = Demo()
Demo.disp()
obj.disp()
