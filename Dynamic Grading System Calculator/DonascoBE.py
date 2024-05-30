import tkinter as tk
import mysql.connector

class Database_Interaction:
    def __init__(self,host,user,password,database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def Create_Database(self,dbname):
        self.cursor_main_database = self.__database.cursor()
        self.cursor_main_database.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
    
    def Set_Database_Info(self, host,user,passwd,database):
        self.__host = host
        self.__user = user
        self.__password = passwd
        self.__database = database
        
    def Get_Database_Info(self):
        return self.__host, self.__user, self.__password, self.__database

class Table_Interaction(Database_Interaction):
    def __init__(self, host, user, password, database, database_reference):
        super().__init__(host, user, password, database)
        self.database_reference = database_reference
    
    def Create_Table(self, host, user, password, database_reference, table_name):
        database_connect = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database_reference,
        )
        cursor = database_connect.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}(userID INT AUTO_INCREMENT PRIMARY KEY)") #HINDI PA ITO TAPOS


class Login_System:
    pass



