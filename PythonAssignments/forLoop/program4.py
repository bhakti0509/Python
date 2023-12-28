'''
Program 4: 
WAP to print all the character values of the given ASCII value range from the user

Input: 
    Enter the start of range : 1
    Enter end of range : -2

Output: 
    Wrong input

Input:
    Enter the start of range : 65
    Enter end of range : 67

Output:
    The character of ASCII value 65 is A
    The character of ASCII value 66 is B
    The character of ASCII value 67 is A
'''

x = int(input("Enter the start of range : "))
y = int(input("Enter the end of range : "))

if (x>=65 or y>=65):
     for i in range(x,y):
        print("The character of ASCII value {} is {}".format(i,chr(i)))
else :
    print("Wrong Input")


