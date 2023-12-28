'''
Program 9: 
WAP to print the count of all negative numbers from a given range

Input: 
    Start : -15
    End : 50

Output:
    15
'''

x = int(input("Enter start : "))
y = int(input("Enter end : "))

count = 0
for i in range(x,y):
    if(i<0):
        count+=1
print(count)

