#Delete Player Data :

import sqlite3;

conn = sqlite3.connect("ipl_teams.db")

cursorObj = conn.cursor()

cursorObj.execute("delete from player where teamName = 'RCB'")

conn.commit()
conn.close()
