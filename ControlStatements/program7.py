# 6) else suite

playerList = ["Rohit","Shubhman","Virat","Ayyar","KLRahul"]

playerName = input("Enter Name of Player: ")

for player in playerList:
    if player == playerName:
        print(playerName,"is present in the list")
        break
else:
    print(playerName,"is not present in the list")
