# Public, Protected, Private (Access Specifiers)

class Demo:

    z = 30

    def __init__(self):
        self._x = 10
        self.__y = 20  #Name mangling => _Demo__y

obj = Demo()
print(obj.z)
print(obj._x)
print(obj._Demo__y)

print(dir(Demo))
print(dir(obj))
