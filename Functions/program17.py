'''
Passing variable number of keyword arguments to a function :
OR
Keyword Arguments

'''

def fun(**argv):
    print(type(argv))
    print(argv)

fun(x = 10, y = 20, z = 30)    
