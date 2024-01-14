'''
WAP defines a class Sum with a mySum method that returns the sum of two numbers.
The program creates two class objects, takes user input to set values for each object,
prints the return sum for both objects, takes user input to set values for each object.

'''

class Sum:

    def __init__(self):
        pass

    def mySum(self,x,y):
        c = x+y
        print("Sum of two numbers : ",c)

def InputFun():

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    return num1,num2

if __name__=="__main__":

        x,y = InputFun()
        obj1 = Sum()
        obj1.mySum(x,y)
        
        a,b = InputFun()
        obj2 = Sum()
        obj2.mySum(a,b)

    



