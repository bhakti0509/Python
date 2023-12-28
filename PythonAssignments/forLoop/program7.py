'''
Program 7:
WAP that prints all positive numbers from a given range.

Input:
    Start : -7
    End : 8

Output:
    1 2 3 4 5 6 7
'''

x = int(input("Enter start : "))
y = int(input("Enter end : "))

for i in range(x,y):
    if(i<=0):
        pass
    else:
        print(i,end = " ")
print()        
