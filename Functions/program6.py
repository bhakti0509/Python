#Returning multiple values from function:

def addByTen(x,y,z):
    x = x+10
    y = y+10
    z = z+10
    return x,y,z

val1 = int(input("Enter value1 : "))
val2 = int(input("Enter value2 : "))
val3 = int(input("Enter value3 : "))

a,b,c = addByTen(val1, val2, val3)

print(a)
print(b)
print(c)
