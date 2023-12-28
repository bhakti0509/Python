def outerFunc():
    print("In outer function")

    def innerFunc1():
        print("In inner function-1")

    def innerFunc2():
        print("In inner function-2")

    return innerFunc1,innerFunc2

'''
#way-1:
ret = outerFunc()
for i in ret:
    i()

#way-2:
ret = outerFunc()
ret[0]()
ret[1]()

'''
#way-3:
ret1,ret2 = outerFunc()
ret1()
ret2()


