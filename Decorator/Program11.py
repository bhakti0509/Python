#Decorator Chaining:

def decorFun(func):
    
    def wrapper():
        print("Start wrapper2")
        func()
        print("End wrapper2")

    return wrapper

def decorFun(func):

    def wrapper():
        print("Start wrapper1")
        func()
        print("End wrapper1")

    return wrapper

@decorFun
@decorFun

def normalFun():
    print("In normal fun")

normalFun()
#normalFun = decorFun(decorFun(normalFun))
