from tkinter import *
from tkinter import messagebox
from PIL import ImageTk     # Python Image Library - ImageTk is used to accept the jpg image files.

def login():
    if username_Entry.get() == '' or password_Entry.get() == '':
        messagebox.showerror('Error', 'Fields Cannot be Empty')
    elif username_Entry.get() == 'Deepak' and password_Entry.get() == '12345':
        messagebox.showinfo('Success', 'Login Successful')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please Enter Correct Credentials')
window=Tk()

window.geometry('1280x700+0+0')
window.resizable(False, False)
window.title('Student Management System - Login Page')

# Creating Background Image

background_Image = ImageTk.PhotoImage(file='bg.jpg')  # Image Tk is only for jpg images.
bg_label = Label(window, image=background_Image)
bg_label.place(x=0, y=0)

# Creating a Frame..

login_Frame = Frame(window, bg='White')
login_Frame.place(x=400, y=150)

logo_Image = PhotoImage(file='logo.png')
logo_Label = Label(login_Frame, image=logo_Image)
logo_Label.grid(row=0, column=0, pady=15)
# User Name
username_Image = PhotoImage(file='user.png')
username_Label = Label(login_Frame, image=username_Image,text='  Username', compound=LEFT, bg='White', font=('times new roman', 16, 'bold'))
username_Label.grid(row = 1, column=0, pady=10, padx=20)
username_Entry=Entry(login_Frame, font=('times new roman', 16, 'bold'), bd=2, fg='Royalblue', relief=GROOVE)
username_Entry.grid(row=1, column=1, pady=10,)
# Password
password_Image = PhotoImage(file = 'password.png')
password_Label=Label(login_Frame, image=password_Image, text = '  Password', compound=LEFT, bg='White', font=('times new roman', 16, 'bold'))
password_Label.grid(row=2, column=0, pady=10, padx=20)
password_Entry=Entry(login_Frame, font=('times new roman', 16, 'bold'), bd=2, fg='Royalblue', relief=GROOVE)
password_Entry.grid(row=2, column=1, pady=15,)
# Button - Login

login_Button = Button(login_Frame, text='Login', font=('times new roman', 14, 'bold'), width=14, bg='Royalblue', fg='White', relief=GROOVE, cursor='hand2', activebackground='Royalblue', activeforeground='White', command=login)
login_Button.grid(row=3, column=0, pady=15, padx=12)
window.mainloop()
