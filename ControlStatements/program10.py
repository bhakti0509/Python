for i in range(10,3,-2):
    print(i)

x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))

for i in range(x, y+1):
    if(i%2==0):
        print("{} is even!".format(i))
    else:
        print("{} is odd!".format(i))
