'''
print: 
    1 
    2 3
    4 5 6
'''
num = 1
for i in range(3):
    for j in range(i+1):
        print(num,end = " ")
        num = num + 1
    print()     
