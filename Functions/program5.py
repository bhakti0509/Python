#Return Statement : 

def factorial(val):
    fact = 1
    for i in range(1,val+1):
        fact = fact*i
    return fact

num = int(input("Enter number : "))

ans = factorial(num)
print("Factorial of {} is {}".format(num,ans))
