'''
Program 3:

Rows = 4

1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

'''
row = int(input("Enter no. of rows : "))

num = 1
for i in range(row):
    for j in range(row):
        print(num,end = " ")
    num = num+1
    print()
