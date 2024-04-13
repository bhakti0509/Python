#Fetching all the data from table :

import sqlite3

conn = sqlite3.connect("ipl_teams.db")

cursorObj = conn.cursor()

cursorObj.execute("select * from Player")

playerData = cursorObj.fetchall()

print(type(playerData))

for i in playerData:
    print(i)

conn.close()
