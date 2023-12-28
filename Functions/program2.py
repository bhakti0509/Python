x = int(input("Enter Number:"))

def sum(a):
    sum = 0
    for i in range(a+1):
        sum = sum + i
    print(sum,end = " ")     
    print()

sum(x)
