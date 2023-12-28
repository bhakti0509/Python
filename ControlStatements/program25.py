'''
print:
    
    A 
    B C
    D E F

'''

num = 65

for i in range(3):
    for j in range(i+1):
        print(chr(num),end = " ")
        num = num + 1
    print()    
