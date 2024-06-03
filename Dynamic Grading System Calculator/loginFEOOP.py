# File para sa front end person 2
# need pa mag pip install customtkinter dito

import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")

class Account_Window_Attributes():
    def __init__(self,title,geometry):
        self.window = customtkinter.CTk() 
        self.title = title
        self.geometry = geometry

class Login_Window(Account_Window_Attributes):
    def __init__(self,title,geometry):
        super().__init__(title,geometry)
 
    
    def create_login_window(self):
        login_window = self.window
        login_window.title(f'{self.title}')
        login_window.geometry(f'{self.geometry}')
        img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
        l1 = customtkinter.CTkLabel(master=login_window, image=img1)
        l1.pack()

        # creating custom frame
        frame = customtkinter.CTkFrame(
            master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(
            master=frame, text="Log into your Account", font=('Century Gothic', 20))
        l2.place(x=50, y=45)

        entry1 = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Username')
        entry1.place(x=50, y=110)

        entry2 = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)

        l3 = customtkinter.CTkLabel(
            master=frame, text="Don't have an account?", font=('Century Gothic', 12))
        l3.place(x=125, y=195)

        # Create custom button
        log_in_button = customtkinter.CTkButton(
            master=frame, width=220, text="Login",command= self.login_function, corner_radius=6) 
        log_in_button.place(x=50, y=240)

        button_register = customtkinter.CTkButton(
            master=frame, width=220, text="Register", corner_radius=6) #command=open_registration,
        button_register.place(x=50, y=290)

        login_window.mainloop()
    
    """def open_registration():
        self.app.destroy()
        self.create_registration_window()"""
    
    def login_function(self): 
        """PANG BACKEND TO!!! FUNCTION TO DASHBOARD NA ITO"""
        self.window.destroy()  # destroy current window and creating new one
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title('Welcome')
        
        l1 = customtkinter.CTkLabel(
            master=w, text="Home Page", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.5,  anchor=tk.CENTER)
        w.mainloop()
        
class Registration_Window(Account_Window_Attributes):
    def __init__(self,title,geometry):
        super().__init__(title,geometry)

    def create_registration_window(self):
        registration_window = self.window  # creating custom tkinter window
        registration_window.geometry(f'{self.geometry}')
        registration_window.title(f'{self.title}')

        img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
        l1 = customtkinter.CTkLabel(master=registration_window, image=img1)
        l1.pack()

        # creating custom frame
        frame = customtkinter.CTkFrame(
            master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(
            master=frame, text="Create a New Account", font=('Century Gothic', 20))
        l2.place(x=50, y=45)

        entry1 = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Username')
        entry1.place(x=50, y=110)

        entry2 = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)

        entry3 = customtkinter.CTkEntry(
            master=frame, width=220, placeholder_text='Confirm Password', show="*")
        entry3.place(x=50, y=220)

        # Create custom button
        button1 = customtkinter.CTkButton(
            master=frame, width=220, text="Register", corner_radius=6)#, command=register_function
        button1.place(x=50, y=275)

        button_back = customtkinter.CTkButton(
            master=frame, width=220, text="Back", corner_radius=6)# command=back_to_login
        button_back.place(x=50, y=310)

        registration_window.mainloop()


'''
THE CODES BELOW AY PANGTESTING LANG NG CLASSES KUNG NAGANA SILA
'''
login = Login_Window('Login','600x440')
registration = Registration_Window('Registration',"600x440")

#login.create_login_window()
registration.create_registration_window()

