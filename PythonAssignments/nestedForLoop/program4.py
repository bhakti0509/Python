'''
Program 5 : 

Row = 4

1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

'''

row = int(input("Enter no. of rows : "))

num = 1
for i in range(row):
    for j in range(row):
        print(num,end = " ")
        num = num + 1
    num = i+2
    print()
