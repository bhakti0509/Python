#Insert into table :

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="ipl_teams")

cursorObj = conn.cursor()

player1 = '''insert into Player values(18,"Virat","RCB","M","IND")'''
player2 = '''insert into Player values(45,"Rohit","MI","M","IND")'''
player3 = '''insert into Player values(96,"Shreyas","DC","M","IND")'''
player4 = '''insert into Player values(41,"Mandhana","RCB","F","IND")'''

cursorObj.execute(player1)
cursorObj.execute(player2)
cursorObj.execute(player3)
cursorObj.execute(player4)

conn.commit()
conn.close()
