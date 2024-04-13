#Python Database Connectivity

#Sqlite3

import sqlite3

conn = sqlite3.connect("ipl_teams.db")
cursorObj = conn.cursor()

createTable = '''
    create table Player(
        
        jerNo integer primary key,
        playername varchar(20),
        teamName varchar(10),
        gender char(1),
        country varchar(20)
    )'''

print(createTable)
cursorObj.execute(createTable)
conn.close()
