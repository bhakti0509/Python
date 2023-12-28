'''
Program 8:
WAP to print numbers which are divisible by 3 and 5 both in a given range.

Input:
    Start : 15
    End : 50

Output:
    15 30 45
'''

x = int(input("Enter start : "))
y = int(input("Enter end : "))

for i in range(x,y):
    if(i%5==0 and i%3==0):
        print(i,end = " ")
print()        
