from DonascoBE import Table_Interaction
from loginFEOOP import Login_Window 
import mysql.connector

dbinfo = {
    "host": "localhost",
    "user": "root",
    "password": "password321"}
dbname = "Dynamic_Grading_System"
table_name = "sheesh" #"sheesh" is sample only. To be coded with dynamic naming later
database_command = mysql.connector.connect(**dbinfo)
database = Table_Interaction(dbinfo['host'],dbinfo['user'],dbinfo['password'],database_command,dbname)


database.Create_Database(dbname)
database.Create_Table(dbinfo['host'],dbinfo['user'],dbinfo['password'],dbname, table_name)

login_Window = Login_Window('Login','600x440')
login_Window.create_login_window()



