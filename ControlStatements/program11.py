x = int(input("Enter 1st no: "))
y = int(input("Enter 2st no: "))

for i in range(x, y+1):
    if(i%4==0 and i%5==0):
        print("{} is divisible by 4 and 5".format(i))
print(i)        
