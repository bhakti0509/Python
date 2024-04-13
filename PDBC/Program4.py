#Update Player Data :

import sqlite3

conn = sqlite3.connect("ipl_teams.db")

cursorObj = conn.cursor()
cursorObj.execute('''update player set playerName = "Virat Kohli" where jerNo = 18''')
conn.commit()
conn.close()
