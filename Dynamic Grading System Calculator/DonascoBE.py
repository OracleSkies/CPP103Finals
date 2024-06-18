#import sqlite3
from CajedaBE import DatabaseManager
from tkinter import messagebox


class Login_System(DatabaseManager):
    def __init__(self, login_username, login_password):
        super().__init__()
        self.login_username = login_username
        self.login_password = login_password

    def login_Account(self):
        cursor = self.database_Connect.cursor()
        sqlCommand = "SELECT * FROM users WHERE username = ? AND password = ?"
        account = (self.login_username, self.login_password)
        cursor.execute(sqlCommand, account)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo("User log in","Account successfully logged in")
        else:
            messagebox.showinfo("User log in","Account not found")

    

class Registration_System(DatabaseManager):
    def __init__(self, reg_Username, reg_Password, reg_Confirm_Pass):
        super().__init__()
        self.reg_Username = reg_Username
        self.reg_Password = reg_Password
        self.reg_Confirm_Pass = reg_Confirm_Pass

    def register_Account(self):
        self.cursor.execute("CREATE TABLE IF NOT EXIST users(\
                            id INTEGER PRIMARY KEY,\
                            username TEXT,\
                            password TEXT NOT NULL)")
        
        if self.reg_Password == self.reg_Confirm_Pass:
            sqlCommand = "INSERT INTO users (username, password) VALUES (?, ?)"
            values = (self.reg_Username, self.reg_Password)
            self.cursor.execute(sqlCommand,values)
            self.conn.commit()
            messagebox.showinfo("Account Registration", "Account Successfully Registered!")
        else:
            messagebox.showinfo("Account Registration", "Password and Confirm Password do not match")



