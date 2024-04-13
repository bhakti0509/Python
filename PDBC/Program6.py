#Python Database Connectivity

#MySQL server

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")

cursorObj = conn.cursor()

createDatabase = "create database if not exists ipl_teams"

cursorObj.execute(createDatabase)

print("Database creted")

conn.close()
