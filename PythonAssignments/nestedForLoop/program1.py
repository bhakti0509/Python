'''
Program 1 : 

Rows = 3

* * *
* * *
* * *

'''

row = int(input("Enter no. of rows : "))

for i in range(row):
    for j in range(row):
        print("*",end = " ")
    print()        
