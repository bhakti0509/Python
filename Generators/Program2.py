def fun():
    yield 10
    yield 20

gen = fun()
print(next(gen))
print(next(gen))
