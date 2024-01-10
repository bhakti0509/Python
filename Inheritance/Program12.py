class Demo:

    def __init__(self):
        print("In constrcutor")

    def __del__(self):
        print("In destructor")

def fun():
    print("In fun")
    obj1 = Demo()
    print("End fun")

fun()
print("End code")
