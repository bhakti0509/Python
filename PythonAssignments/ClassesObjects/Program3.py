'''
Write a real time example of oop which contains the following point:
a) Instance variable
b) constructor
c) class variable
d) Instance method

'''

class Friends:

    room = 'Common room for all'

    def __init__(self):

        self.money = 5000
        self.laptop = 'Personal laptop'
    
    def friendInfo(self):
        print(self.money)
        print(self.laptop)

    def study(self):
        
        print(self.room)
        print("Everyone is studying!")

obj = Friends()
obj.friendInfo()
obj.study()



