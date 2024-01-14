'''
WAP that defines a parent function with two nested functions(myIndex and myPalindrome). 
The program prompts the user to choose betweet these two functions and then calls the selected 
function based on the user's input.

'''

def parent():

    def myIndex():
        print("In function : myIndex")        

    def myPalindrome():
        print("In function : myPalindrome")
    
    return myIndex, myPalindrome


retObj1, retObj2 = parent()

print("Functions : ")
print("1. MyIndex")
print("2. MyPalindrome")

choice = input("Enter the function number which you want to perform : ")

if(choice == '1'):
    retObj1()

elif(choice == '2'):
    retObj2()

else:
    print("Invalid choice!")

