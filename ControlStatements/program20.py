#o/p : 5 * 15 * 25 * 35 * 45 *

x = 50

for i in range(5,x+1,5):
    if(i%2==0):
        print("*",end = " ")
    else:
        print(i,end = " ")

print()        

