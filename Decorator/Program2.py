def outerFunc():
    print("In outer function")

    def innerFunc1():
        print("In inner function-1")

    def innerFunc2():
        print("In inner function-2")

    innerFunc1()
    innerFunc2()

outerFunc()
