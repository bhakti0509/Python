'''Passing variable number of arguments to a function:
   OR
   Varargs
'''

def fun(*argv):
    for i in argv:
        print(i)

fun(10,20,30,40)        
