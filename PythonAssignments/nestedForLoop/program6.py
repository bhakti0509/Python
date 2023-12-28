'''
Program 6 : 

Rows = 4

1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

'''

row = int(input("Enter no. of rows : "))

for i in range(row):
    num = 1
    for j in range(row):
        print(num,end = " ")
        num = num+1
    print()     
