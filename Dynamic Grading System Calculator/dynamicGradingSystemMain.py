from DonascoBE import Table_Interaction
from PadillaFE import Registration_Window 
import mysql.connector

dbinfo = {
    "host": "localhost",
    "user": "root",
    "password": "password321"}
dbname = "Dynamic_Grading_System"

database_command = mysql.connector.connect(**dbinfo)
database = Table_Interaction(dbinfo['host'],dbinfo['user'],dbinfo['password'],database_command,dbname)

database.Create_Database(dbname)

registration_Window = Registration_Window(dbinfo['host'],dbinfo['user'],dbinfo['password'],database_command,dbname)

registration_Window.mainloop()

