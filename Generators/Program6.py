def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30 
    yield 
    print("End fun") 

ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))


