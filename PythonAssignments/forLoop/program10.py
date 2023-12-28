'''
Program 10:
WAP to calculate and print the product of the count of odd numbers within a given range

Input:
    Start : 1
    End : 11

Output: 
    3125
'''

x = int(input("Enter Start : "))
y = int(input("Enter end : "))

count = 1
for i in range(x,y):
    if(i%2==1):
        count = count*i
print(count)        
