#Update data : 

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="ipl_teams")

cursorObj = conn.cursor()

cursorObj.execute('''update Player set playerName="Smriti Mandhana" where jerNo=41''')

conn.commit()
conn.close()
