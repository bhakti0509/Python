#o/p : 1*3*5*7*9*

x = 10
for i in range (1,x+1):
    if(i%2!=0):
        print(i,end = " ")
    else:
        print("*",end =" ")
