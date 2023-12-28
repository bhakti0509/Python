num = int(input("Enter number : "))

def divby4and5(x):
    if(x%4 == 0 and x%5 == 0):
        print("{} is divisible by 4 and 5".format(x))
    else:
        print("{} is not divisible by 4 and 5".format(x))

divby4and5(num)
