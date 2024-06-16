import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

header_Font = ('Century Gothic', 20)
label_Font = ('Century Gothic', 12)
#================================ L O G I N   W I N D O W    C L A S S E S ======================================
class Login_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(width=320, height=360, corner_radius=15)

        self.header_Label = customtkinter.CTkLabel(self, text="Log into your Account", font= header_Font)
        self.header_Label.place(x=50, y=45)

        self.username_Entry_Box = customtkinter.CTkEntry(self, width=220, placeholder_text='Username')
        self.username_Entry_Box.place(x=50, y=110)

        self.password_Entry_Box = customtkinter.CTkEntry(self, width=220, placeholder_text='Password', show="*")
        self.password_Entry_Box.place(x=50, y=165)

        self.for_Registration_Label = customtkinter.CTkLabel(self, text="Don't have an account?", font=label_Font)
        self.for_Registration_Label.place(x=125, y=195)

        self.log_In_Button = customtkinter.CTkButton(self, width=220, text="Login", corner_radius=6) #command= self.login_function
        self.log_In_Button.place(x=50, y=240)

        self.button_Register = customtkinter.CTkButton(self, width=220, text="Register", corner_radius=6) #command=open_registration,
        self.button_Register.place(x=50, y=290)

class Login_Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry('600x440')
        self.background_Image = ImageTk.PhotoImage(Image.open("pattern.png"))
        self.bg_Image_Label = customtkinter.CTkLabel(self, image=self.background_Image)
        self.bg_Image_Label.pack()

        self.login_Frame = Login_Frame(master=self)
        self.login_Frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER )

#======================= R E G I S T R A T I O N   W I N D O W    C L A S S E S ======================================

class Registration_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(self, width=320, height=360, corner_radius=15)

        self.header_Label = customtkinter.CTkLabel(self, text="Create a New Account", font=header_Font)
        self.header_Label.place(x=50, y=45)

        self.username_Entry_Box = customtkinter.CTkEntry(self, width=220, placeholder_text='Username')
        self.username_Entry_Box.place(x=50, y=110)

        self.password_Entry_Box = customtkinter.CTkEntry(self, width=220, placeholder_text='Password', show="*")
        self.password_Entry_Box.place(x=50, y=165)

        self.confirm_password_Entry_Box = customtkinter.CTkEntry(self, width=220, placeholder_text='Confirm Password', show="*")
        self.confirm_password_Entry_Box.place(x=50, y=220)

        #command=register_function
        self.register_Button = customtkinter.CTkButton(self, width=220, text="Register", corner_radius=6)
        self.register_Button.place(x=50, y=275)

        #command=back_to_login
        self.back_Button = customtkinter.CTkButton(self, width=220, text="Back", corner_radius=6)
        self.back_Button.place(x=50, y=310)


class Registration_Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x440")
        self.title('Registration')

        self.background_Image = ImageTk.PhotoImage(Image.open("pattern.png"))
        self.bg_Image_Label = customtkinter.CTkLabel(self, image=self.background_Image)
        self.bg_Image_Label.pack()

        self.registration_Frame = Registration_Frame(master = self)
        self.registration_Frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

