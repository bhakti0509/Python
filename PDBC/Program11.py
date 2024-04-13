#Delete from a table:

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="ipl_teams")

cursorObj = conn.cursor()

cursorObj.execute('''delete from Player where teamName="MI"''')

conn.commit()
conn.close()
