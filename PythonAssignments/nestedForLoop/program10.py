'''
Program 19 : 

Row = 4

1   3   5   7
5   7   9   11
9   11  13  15
13  15  17  19

'''

row = int(input("Enter no. of rows : "))

num = 1

for i in range(row):
    for j in range(row):
        print(num,end = " ")
        num = num+2
    num = num-4
    print()
