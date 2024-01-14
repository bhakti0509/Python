'''
Write a real time example of OOP on IPL cricket by the following point:

    a) Instance variable
    b) Constructor
    c) Class variable
    d) Instance method
'''

class IPL:
    
    team = 'RCB'
    captain = 'Virat Kohali'

    def __init__(self):

        self.player = 'Virat Kohali'
        self.jerNo = 18
    
    def playerInfo(self):
        
        print("Information of the player : ")
        print(self.player)
        print(self.jerNo)

obj = IPL()
print(IPL.team)
print(IPL.captain)
obj.playerInfo()

