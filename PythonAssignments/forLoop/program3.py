'''
Program 3: 
WAP to print sum of all numbers from a given range.

Input: 
    start = 1
    end = 10

Output:
    45
'''

x = int(input("Enter value for x : "))
y = int(input("Enter value for y : "))

sum = 0
for i in range(x,y):
    sum = sum+i
print(sum,end = " ")

print()
