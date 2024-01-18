class Demo:
    def fun(self):
        print("In Demo : fun")

class Demo1():
    def fun(self):
        print("In Demo1 : fun")

def callFun(obj):
    obj.fun()

obj1 = Demo()
obj2 = Demo1()

callFun(obj2)
