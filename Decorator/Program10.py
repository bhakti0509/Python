def decorFun(func):
    print("In decorfun")

    def wrapper(*args):
        print("Start wrapper")
        val = func(*args)
        print("End wrapper")
        return val

    return wrapper

@decorFun

def normalFun(x,y):
    print("In normal fun")
    return x+y

#normalFun = decorFun(normalFun(10,20))
print(normalFun(10,20))

