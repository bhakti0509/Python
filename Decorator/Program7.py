#using DecorFun
#Function Decorator

def normalFun(Func):
    def wrapper():
        print("Start wrapper")
        Func()
        print("End wrapper")
    return wrapper

@decorFun

def normalFun():
    print("Hello in normal fun")

#normalFun = decorFun(normalFun)
#normalFun()
