class Parent:

    def fun(self):
        print("In fun : Parent")

class Parent1(Parent):
    
    pass

class Parent2(Parent):

    def fun(self):
        print("In fun : Parent2")

class Child(Parent1,Parent2):
    pass

obj = Child()
obj.fun()
