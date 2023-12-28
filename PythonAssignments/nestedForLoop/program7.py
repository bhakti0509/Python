'''
Program 7 :

Row = 3

1   3   5
7   9   11
13  15  17

'''

row = int(input("Enter no. of rows :  "))

num = 1
for i in range(row):
    for j in range(row):
        print(num, end = "  ")
        num = num+2
    print()    
