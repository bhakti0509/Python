#Insert into table Player :

import sqlite3

conn = sqlite3.connect("ipl_teams.db")

cursorObj = conn.cursor()

player1 = '''insert into Player values(18, 'Virat', 'RCB', 'M', 'IND')'''
player2 = '''insert into Player values(45, 'Rohit', 'MI', 'M', 'IND')'''
player3 = '''insert into Player values(41, 'Smriti', 'RCB', 'F','IND')'''
player4 = '''insert into Player values(12, 'Perry', 'RCB', 'F','AUS')'''

cursorObj.execute(player1)
cursorObj.execute(player2)
cursorObj.execute(player3)
cursorObj.execute(player4)

conn.commit()
conn.close()

