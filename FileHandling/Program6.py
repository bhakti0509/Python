#reading of a file : 1)read() function

f1 = open("Core2Web.txt","r+")
print(f1.read())
print(f1.tell())
print(f1.read())
print(f1.tell())