#Fetching data from server :

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="ipl_teams")

cursorObj = conn.cursor()

cursorObj.execute("select * from Player")

for i in cursorObj :
    print(i)
