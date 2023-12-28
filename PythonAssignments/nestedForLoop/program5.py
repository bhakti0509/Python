'''
Program 6 : 

Rows = 5

# # # # #
@ @ @ @ @
# # # # #
@ @ @ @ @
# # # # #

'''

row = int(input("Enter no. of rows : "))

for i in range(row):
    for j in range(row):
        if(i%2==1):
            print("@",end = " ")
        else:
            print("#",end = " ")
    print()        
