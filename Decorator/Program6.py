def decorFun(Func):
    def wrapper():
        print("Start wrapper")
        Func()
        print("End wrapper")

    return wrapper

def normalFun():
    print("Hello in normal fun")

retFun = decorFun(normalFun)
retFun()
