def outer():
    def inner1():
        print("In inner1 fun")

    inner2()     #Error:- UnboundLocalError : local variable 'inner2' referenced before assignment 

    def inner2():
        print("In inner2 fun")
    print("In outer function")

outer()
