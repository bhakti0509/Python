class Demo1:
    def fun(self):
        print("In Demo1 : fun")

class Demo2:
    def gun(self):
        print("In Demo2 : gun")

def callFun(obj):
    if hasattr(obj,'fun'):
        obj.fun()
    elif hasattr(obj,'gun'):
        obj.gun()

obj1 = Demo1()
obj2 = Demo2()

callFun(obj2)

