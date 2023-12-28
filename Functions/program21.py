print("Function")

def outer():
    def inner1():
        print("In inner1 function")
    def inner2():
        print("In inner2 function")

    print("In outer function")

outer().inner1()   #Error : AttributeError 
