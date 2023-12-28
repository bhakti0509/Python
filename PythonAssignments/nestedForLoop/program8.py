'''
Program 8 :

Row = 3

1 3 5
1 3 5
1 3 5

'''

row = int(input("Enter no. of rows : "))

for i in range(row):
    num = 1
    for j in range(row):
        print(num,end = " ")
        num = num+2
    print()     
