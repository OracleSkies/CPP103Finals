#import sqlite3
from CajedaBE import DatabaseManager
from tkinter import messagebox


class Login_System(DatabaseManager):
    def __init__(self, login_username, login_password,window):
        super().__init__()
        self.login_username = login_username
        self.login_password = login_password
        self.window = window

    def login_Account(self):
        sqlCommand = "SELECT * FROM users WHERE username = ? AND password = ?"
        account = (self.login_username, self.login_password)
        self.cursor.execute(sqlCommand, account)
        result = self.cursor.fetchone()
        if result:
            messagebox.showinfo("User log in","Account successfully logged in")
            self.window.destroy()
        else:
            messagebox.showinfo("User log in","Account not found")

    

class Registration_System(DatabaseManager):
    def __init__(self, reg_Username, reg_Password, reg_Confirm_Pass,window):
        super().__init__()
        self.reg_Username = reg_Username
        self.reg_Password = reg_Password
        self.reg_Confirm_Pass = reg_Confirm_Pass
        self.window = window

    def register_Account(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                            id INTEGER PRIMARY KEY,\
                            username TEXT,\
                            password TEXT NOT NULL)")
        if self.reg_Password == self.reg_Confirm_Pass:
            sqlCommand = "INSERT INTO users (username, password) VALUES (?, ?)"
            values = (self.reg_Username, self.reg_Password)
            self.cursor.execute(sqlCommand,values)
            self.conn.commit()
            messagebox.showinfo("Account Registration", "Account Successfully Registered!")
            self.window.destroy()
        else:
            messagebox.showinfo("Account Registration", "Password and Confirm Password do not match")



