def gun():
    print("In gun")

def run(y):
    print("In run")
    y()

def fun(x):
    print("In fun")
    #x() #TypeError : 'NoneType' object is not callable

fun(run(gun))
