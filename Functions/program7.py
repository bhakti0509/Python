def addByTen(x,y,z):
    x = x+10
    y = y+10
    z = z+10
    return x,y,z

val1 = int(input("Enter value1 : "))
val2 = int(input("Enter value2 : "))
val3 = int(input("Enter value3 : "))

retval = addByTen(val1, val2, val3)
print(type(retval))

for i in retval:
    print(i)
