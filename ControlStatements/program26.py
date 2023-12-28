'''
print:

    1 2 3
    4 5 
    6

'''
num = 1
row = int(input("Enter no. of rows : "))

for i in range(row):
    for j in range(row-i):
        print(num,end =" ")
        num+=1
    print()    
