import mysql.connector
from tkinter import messagebox

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

        self.database_Connect = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database_reference,
        )


class Login_System:
    pass

class Registration_System(Table_Interaction):
    def __init__(self, host, user, password, database, database_reference, reg_Username, reg_Password, reg_Confirm_Pass):
        super().__init__(host, user, password, database, database_reference)
        self.reg_Username = reg_Username
        self.reg_Password = reg_Password
        self.reg_Confirm_Pass = reg_Confirm_Pass

    def register_Account(self):
        cursor = self.database_Connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registered_Users (\
                       userID INT AUTO_INCREMENT PRIMARY KEY,\
                       username VARCHAR(255),\
                       password VARCHAR(255))")
        
        if self.reg_Password == self.reg_Confirm_Pass:
            sqlCommand = "INSERT INTO registered_Users (username, password) VALUES (%s, %s)"
            values = (self.reg_Username, self.reg_Password)
            cursor.execute(sqlCommand,values)
            self.database_Connect.commit()
            messagebox.showinfo("Account Registration", "Account Successfully Registered!")
        else:
            messagebox.showinfo("Account Registration", "Password and Confirm Password do not match")



