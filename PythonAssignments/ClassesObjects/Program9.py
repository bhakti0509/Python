''' WAP that returns the count of the search element in the list.'''

def Search(List):

    x = int(input("Enter the number to be search for its count : "))

    '''elecount = 0

    for i in List:
        if i==x:
            elecount += 1
    return elecount,x '''      

    my_listCount = List.count(x)
    return my_listCount,x

if __name__=="__main__":

    List = []

    n = int(input("Enter the count of elements to add in the list : "))

    for i in range(0,n):
        ele = int(input())
        List.append(ele) 

    print(List)

    count,y = Search(List)
    
    print("Count of {} is {}".format(y,count))




