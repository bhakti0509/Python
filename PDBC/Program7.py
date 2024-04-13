#Creating Tables :

import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="",database="ipl_teams")

cursorObj = conn.cursor()

createTable = '''
    
    create table Player(
        
        jerNo integer primary key,
        playerName varchar(30),
        teamName varchar(20),
        gender char(1),
        country varchar(10)
    )
    '''

cursorObj.execute(createTable)

conn.commit()
conn.close()
