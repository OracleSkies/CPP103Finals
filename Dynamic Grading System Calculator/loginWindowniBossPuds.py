# File para sa front end person 2
# need pa mag pip install customtkinter dito

import tkinter
import customtkinter
from PIL import ImageTk, Image

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("green")


def create_login_window():
    app = customtkinter.CTk()  # creating custom tkinter window
    app.geometry("600x440")
    app.title('Login')

    def open_registration():
        app.destroy()
        create_registration_window()

    def login_function():
        app.destroy()  # destroy current window and creating new one
        w = customtkinter.CTk()
        w.geometry("1280x720")
        w.title('Welcome')
        l1 = customtkinter.CTkLabel(
            master=w, text="Home Page", font=('Century Gothic', 60))
        l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
        w.mainloop()

    img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)
    l1.pack()

    # creating custom frame
    frame = customtkinter.CTkFrame(
        master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

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
    button1 = customtkinter.CTkButton(
        master=frame, width=220, text="Login", command=login_function, corner_radius=6)
    button1.place(x=50, y=240)

    button_register = customtkinter.CTkButton(
        master=frame, width=220, text="Register", command=open_registration, corner_radius=6)
    button_register.place(x=50, y=290)

    app.mainloop()


def create_registration_window():
    app = customtkinter.CTk()  # creating custom tkinter window
    app.geometry("600x440")
    app.title('Registration')

    def back_to_login():
        app.destroy()
        create_login_window()

    def register_function():
        # Function to handle registration logic
        username = entry1.get()
        password = entry2.get()
        confirm_password = entry3.get()

        if password == confirm_password:
            print(f"Registered with Username: {username}")
            # Add code to save user info or authenticate here
            # Example: Save to a file or database
        else:
            print("Passwords do not match!")

    img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
    l1 = customtkinter.CTkLabel(master=app, image=img1)
    l1.pack()

    # creating custom frame
    frame = customtkinter.CTkFrame(
        master=l1, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

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
        master=frame, width=220, text="Register", command=register_function, corner_radius=6)
    button1.place(x=50, y=275)

    button_back = customtkinter.CTkButton(
        master=frame, width=220, text="Back", command=back_to_login, corner_radius=6)
    button_back.place(x=50, y=310)

    app.mainloop()


create_login_window()
