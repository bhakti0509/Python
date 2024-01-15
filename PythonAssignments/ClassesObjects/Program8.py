'''
Write a parent function that includes the nested functions digitCount, 
evenDigitCount, oddDigitCount. Prompt the user to choose the desired function
and provide a list of elements. Then, invoke the selected function based on
the user's choice and the input list.

'''

def parent(List):
    
    def digitCount():
        size = len(List)
        print("Total number of digits in the list : ",size)
            
    def evenDigitCount():
        even_count = 0
        for i in List:
            if i%2 == 0:
                even_count += 1

        print("Total number of even digits in the list : ",even_count)    


    def oddDigitCount():
        odd_count = 0
        for i in List:
            if i%2 == 1:
                odd_count += 1

        print("Total number of odd digits in the list : ",odd_count)


def main():
    
    elements = []

    n = int(input("Enter the elements to add in the list :  "))
    for i in range(0, n):
        ele = int(input())
        elements.append(ele)

    while True:

        print("1. DigitCount")
        print("2. EvenDigitCount") 
        print("3. OddDigitCount") 
        print("4. Exit")

        retObj1, retObj2, retObj3 = parent(elements)

        choice = input("Enter your choice : ")

        if choice == '1':
            retObj1()

        elif choice == '2':
            retObj2()

        elif choice == '3':
            retObj3()

        elif choice == '4':
            print("Bye!")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
    
