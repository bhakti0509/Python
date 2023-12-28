'''
Program 2 : 

Rows = 4

1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

'''

row = int(input("Enter no. of rows : "))
num = 1

for i in range(row):
    for j in range(row-1):
        print(num,end = "   ")
        num = num+1;
    print()    
