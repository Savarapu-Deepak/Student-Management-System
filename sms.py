from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas
count = 0
text = ''
con = pymysql.connect(host='localhost', user='root', password='Deepak@1997', database='Student_management_system')
mycursor = con.cursor()
def exit():
    result=messagebox.askyesno('Confirm', 'Do you want to Exit.?')
    if result:
        root.destroy()
    else:
        pass
def export_Data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_Table.get_children()
    newlist=[]
    for index in indexing:
        content=student_Table.item(index)
        data_list=content['values']
        newlist.append(data_list)
    table=pandas.DataFrame(newlist, columns=['ID', 'Name', 'GENDER', 'CLASS', 'MOBILE', 'EAMAIL', 'ADDRESS', 'DATE', 'CURR_TIME'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data Saved Successfully')
def update_Student():
    def update_Data():
        query = "UPDATE STUDENT_DATA SET NAME=%s, GENDER=%s, CLASS=%s, MOBILE=%s, EMAIL=%s, ADDRESS=%s, DATE=%s, TIME=%s where ID=%s"
        mycursor.execute(query, (name_Entry.get(), gender_Entry.get(), class_Entry.get(), mobile_Entry.get(), email_Entry.get(), address_Entry.get(), date, curr_Time, id_Entry.get()))
        con.commit()
        messagebox.showinfo('Success', f'ID {id_Entry.get()} is Updated Successfully', parent=update_Window)
        update_Window.destroy()
        show_Student()
    update_Window = Toplevel()
    update_Window.title('Update Student')
    update_Window.resizable(False, False)
    update_Window.grab_set()
    id_Label = Label(update_Window, text='ID', font=('times new roman', 20, 'bold'))
    id_Label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    id_Entry.grid(row=0, column=1, pady=15, padx=10)

    name_Label = Label(update_Window, text='NAME', font=('times new roman', 20, 'bold'))
    name_Label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    name_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    name_Entry.grid(row=1, column=1, padx=10)

    gender_Label = Label(update_Window, text='GENDER', font=('times new roman', 20, 'bold'))
    gender_Label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    gender_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    gender_Entry.grid(row=2, column=1, padx=10)

    class_Label = Label(update_Window, text='CLASS', font=('times new roman', 20, 'bold'))
    class_Label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    class_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    class_Entry.grid(row=3, column=1, padx=10)

    mobile_Label = Label(update_Window, text='MOBILE', font=('times new roman', 20, 'bold'))
    mobile_Label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mobile_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    mobile_Entry.grid(row=4, column=1, padx=10)

    email_Label = Label(update_Window, text='EMAIL', font=('times new roman', 20, 'bold'))
    email_Label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    email_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    email_Entry.grid(row=5, column=1, padx=10)

    address_Label = Label(update_Window, text='ADDRESS', font=('times new roman', 20, 'bold'))
    address_Label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    address_Entry = Entry(update_Window, font=('roman', 15, 'bold'), width=24)
    address_Entry.grid(row=6, column=1, padx=10)

    student_Button = ttk.Button(update_Window, text='UPDATE STUDENT', command=update_Data)
    student_Button.grid(row=7, columnspan=2, pady=15)

    indexing = student_Table.focus()
    content = student_Table.item(indexing)
    list_data=content['values']
    id_Entry.insert(0, list_data[0])
    name_Entry.insert(0, list_data[1])
    gender_Entry.insert(0, list_data[2])
    class_Entry.insert(0, list_data[3])
    mobile_Entry.insert(0, list_data[4])
    email_Entry.insert(0, list_data[5])
    address_Entry.insert(0, list_data[6])

def show_Student():
    query = "SELECT * FROM STUDENT_DATA"
    mycursor.execute(query)
    fetched_Data = mycursor.fetchall()
    student_Table.delete(*student_Table.get_children())
    for data in fetched_Data:
        student_Table.insert('', END, values=data)
def delete_Student():
    indexing = student_Table.focus()
    index_Content = student_Table.item(indexing)
    content_ID = index_Content['values'][0]
    query = "DELETE FROM STUDENT_DATA WHERE ID=%s"
    mycursor.execute(query, content_ID)
    con.commit()
    messagebox.showinfo('Deleted', f'ID {content_ID} is Deleted Successfully')
    query = "SELECT * FROM STUDENT_DATA"
    mycursor.execute(query)
    fetched_Data = mycursor.fetchall()
    student_Table.delete(*student_Table.get_children())
    for data in fetched_Data:
        student_Table.insert('', END, values=data)
def search_Student():
    def search_Data():
        query = "SELECT * FROM STUDENT_DATA WHERE ID=%s or NAME=%s or GENDER=%s or CLASS=%s or MOBILE=%s or EMAIL=%s or ADDRESS=%s"
        mycursor.execute(query, (id_Entry.get(), name_Entry.get(), gender_Entry.get(), class_Entry.get(), mobile_Entry.get(), email_Entry.get(), address_Entry.get()))
        student_Table.delete(*student_Table.get_children())
        fetched_Data = mycursor.fetchall()
        for data in fetched_Data:
            student_Table.insert('', END, values=data)

    search_Window = Toplevel()
    search_Window.title('Search Student')
    search_Window.resizable(False, False)
    search_Window.grab_set()
    id_Label = Label(search_Window, text='ID', font=('times new roman', 20, 'bold'), )
    id_Label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    id_Entry.grid(row=0, column=1, pady=15, padx=10)

    name_Label = Label(search_Window, text='NAME', font=('times new roman', 20, 'bold'))
    name_Label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    name_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    name_Entry.grid(row=1, column=1, padx=10)

    gender_Label = Label(search_Window, text='GENDER', font=('times new roman', 20, 'bold'))
    gender_Label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    gender_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    gender_Entry.grid(row=2, column=1, padx=10)

    class_Label = Label(search_Window, text='CLASS', font=('times new roman', 20, 'bold'))
    class_Label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    class_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    class_Entry.grid(row=3, column=1, padx=10)

    mobile_Label = Label(search_Window, text='MOBILE', font=('times new roman', 20, 'bold'))
    mobile_Label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mobile_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    mobile_Entry.grid(row=4, column=1, padx=10)

    email_Label = Label(search_Window, text='EMAIL', font=('times new roman', 20, 'bold'))
    email_Label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    email_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    email_Entry.grid(row=5, column=1, padx=10)

    address_Label = Label(search_Window, text='ADDRESS', font=('times new roman', 20, 'bold'))
    address_Label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    address_Entry = Entry(search_Window, font=('roman', 15, 'bold'), width=24)
    address_Entry.grid(row=6, column=1, padx=10)

    student_Button = ttk.Button(search_Window, text='SEARCH STUDENT', command=search_Data)
    student_Button.grid(row=7, columnspan=2, pady=15)

def add_Student():
    def add_Data():
        if id_Entry.get() == '' or name_Entry.get() == '' or gender_Entry.get() == '' or class_Entry.get() == '' or mobile_Entry.get() == '' or email_Entry.get() == '' or address_Entry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required')
        else:
            try:
                query = "INSERT INTO STUDENT_DATA VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(query, (id_Entry.get(), name_Entry.get(), gender_Entry.get(), class_Entry.get(), mobile_Entry.get(), email_Entry.get(), address_Entry.get(), date, curr_Time))
                con.commit()
                result = messagebox.askyesno('Success', 'Data Added Successfully. Do you want to clean the form.?')
                if result:
                    id_Entry.delete(0, END)
                    name_Entry.delete(0, END)
                    gender_Entry.delete(0, END)
                    class_Entry.delete(0, END)
                    mobile_Entry.delete(0, END)
                    email_Entry.delete(0, END)
                    address_Entry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'ID cannot be repeated', parent=add_Window)
                return
            query = "SELECT * FROM STUDENT_DATA"
            mycursor.execute(query)
            fetch_Data = mycursor.fetchall()
            student_Table.delete(*student_Table.get_children())
            for data in fetch_Data:
                student_Table.insert('', END, values=data)

    add_Window= Toplevel()
    add_Window.resizable(False, False)
    add_Window.grab_set()
    id_Label = Label(add_Window, text='ID', font=('times new roman', 20, 'bold'), )
    id_Label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    id_Entry.grid(row=0, column=1, pady=15, padx=10)

    name_Label = Label(add_Window, text='NAME', font=('times new roman', 20, 'bold'))
    name_Label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    name_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    name_Entry.grid(row=1, column=1, padx=10)

    gender_Label = Label(add_Window, text='GENDER', font=('times new roman', 20, 'bold'))
    gender_Label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    gender_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    gender_Entry.grid(row=2, column=1, padx=10)

    class_Label = Label(add_Window, text='CLASS', font=('times new roman', 20, 'bold'))
    class_Label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    class_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    class_Entry.grid(row=3, column=1, padx=10)

    mobile_Label = Label(add_Window, text='MOBILE', font=('times new roman', 20, 'bold'))
    mobile_Label.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    mobile_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    mobile_Entry.grid(row=4, column=1, padx=10)

    email_Label = Label(add_Window, text='EMAIL', font=('times new roman', 20, 'bold'))
    email_Label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    email_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    email_Entry.grid(row=5, column=1, padx=10)

    address_Label = Label(add_Window, text='ADDRESS', font=('times new roman', 20, 'bold'))
    address_Label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    address_Entry = Entry(add_Window, font=('roman', 15, 'bold'), width=24)
    address_Entry.grid(row=6, column=1, padx=10)
    student_Button = ttk.Button(add_Window, text= 'ADD STUDENT', command=add_Data)
    student_Button.grid(row=7, columnspan=2, pady=15)

def connect_DB():
    global mycursor, con
    def connect():
        # global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password='Deepak@1997')
            mycursor = con.cursor()
            messagebox.showinfo('Successes', 'Connected to Database', parent=db_Window)
            db_Window.destroy()
        except:
            messagebox.showerror('Sorry', 'Database Connection Failed !', parent=db_Window)
        try:
            query = "CREATE DATABASE STUDENT_MANAGEMENT_SYSTEM"
            mycursor.execute(query)
            query = "USE STUDENT_MANAGEMENT_SYSTEM"
            mycursor.execute(query)
            query = "CREATE TABLE STUDENT_DATA(ID VARCHAR(5) NOT NULL PRIMARY KEY, NAME VARCHAR(30), GENDER VARCHAR(1), CLASS VARCHAR(3), MOBILE VARCHAR(10), EMAIL VARCHAR(30), ADDRESS VARCHAR(30), DATE VARCHAR(30), TIME VARCHAR(30))"
            mycursor.execute(query)
        except:
            query = "USE STUDENT_MANAGEMENT_SYSTEM"
            mycursor.execute(query)
        add_Student_Button.config(state=NORMAL)
        search_Student_Button.config(state=NORMAL)
        delete_Student_Button.config(state=NORMAL)
        update_Student_Button.config(state=NORMAL)
        show_Student_Button.config(state=NORMAL)
        export_Data_Button.config(state=NORMAL)
        exit_Button.config(state=NORMAL)
    db_Window = Toplevel()
    db_Window.geometry('470x250+730+230')
    db_Window.title('Database Connection')
    db_Window.grab_set()
    db_Window.resizable(0, 0)
    host_Name = Label(db_Window, text = ' Host Name ', font=('arial', 16, 'bold'))
    host_Name.grid(row=0, column=0, padx= 20, pady=15)
    host_Name_Entry = Entry(db_Window, font=('roman', 15, 'bold'), bd=2)
    host_Name_Entry.grid(row=0, column=1, padx=20)

    user_Name = Label(db_Window, text='User Name ', font=('arial', 16, 'bold'))
    user_Name.grid(row=1, column=0, padx=20, pady=15)
    user_Name_Entry = Entry(db_Window, font=('roman', 15, 'bold'), bd=2)
    user_Name_Entry.grid(row=1, column=1, padx=20)

    Password = Label(db_Window, text='Password ', font=('arial', 16, 'bold'))
    Password.grid(row=2, column=0, padx=20, pady=15)
    Password_Entry = Entry(db_Window, font=('roman', 15, 'bold'), bd=2)
    Password_Entry.grid(row=2, column=1, padx=15)

    db_Connect = ttk.Button(db_Window, text='Connect', command=connect)
    db_Connect.grid(row=3, column=0, pady=8)

def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    slider_.config(text=text)
    count += 1
    slider_.after(300, slider)

def clock():
    global date, curr_Time
    date = time.strftime('%d/%m/%Y')
    curr_Time = time.strftime('%H:%M:%S')
    date_Time.config(text=f'     Date : {date}\n Time : {curr_Time}')
    date_Time.after(1000, clock)

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700+0+0')
root.title('Student Management System - Dashboard')
root.resizable(False, False)
date_Time = Label(root, font=('times new roman', 18, ' italic bold'))
date_Time.place(x=5, y=5)
clock()

# Slider Label.....
s = 'STUDENT MANAGEMENT SYSTEM'
slider_ = Label(root, text=s, font=('times new roman', 26, 'italic bold'), pady=10)
slider_.place(x=320, y=0)
slider()

db_BUtton = ttk.Button(root, text='Connect Database', padding=15, command=connect_DB)
db_BUtton.place(x=1050, y=0)

left_Frame = Frame(root)
left_Frame.place(x=60, y=100, height=570, width = 250)

student_image = PhotoImage(file='student (1).png')
student_image_Label = Label(left_Frame, image=student_image, compound=LEFT)
student_image_Label.grid(row=0, column=0, padx=5)

add_Student_Button = ttk.Button(left_Frame, text='Add Student', width = 25, command=add_Student)
add_Student_Button.grid(row=1, column=0, pady=15, padx=5)

search_Student_Button = ttk.Button(left_Frame, text='Search Student', width =25, command=search_Student)
search_Student_Button.grid(row=2, column=0, pady=15, padx=5)

delete_Student_Button = ttk.Button(left_Frame, text = 'Delete Student', width=25, command=delete_Student)
delete_Student_Button.grid(row=3, column=0, pady=15, padx=5)

update_Student_Button = ttk.Button(left_Frame, text='Update Student', width=25, command=update_Student)
update_Student_Button.grid(row=4, column=0, pady=15, padx=5)

show_Student_Button = ttk.Button(left_Frame, text='Show Student', width=25, command=show_Student)
show_Student_Button.grid(row=5, column=0, pady=15, padx=5)

export_Data_Button = ttk.Button(left_Frame, text='Export Data', width=25, command=export_Data)
export_Data_Button.grid(row=6, column=0, pady=15)

exit_Button = ttk.Button(left_Frame, text='Exit', width=25, command=exit)
exit_Button.grid(row=7, column=0, pady=15)

right_Frame = Frame(root)
right_Frame.place(x=350, y=100, height=570, width = 850)

scroll_Bar_X = Scrollbar(right_Frame, orient= HORIZONTAL)
scroll_Bar_y = Scrollbar(right_Frame, orient= VERTICAL)

scroll_Bar_X.pack(side=BOTTOM, fill=X)
scroll_Bar_y.pack(side=RIGHT, fill=Y)

student_Table = ttk.Treeview(right_Frame, columns=('Id', 'Name', 'Gender', 'Class', 'Mobile.No', 'Email-id', 'Address', 'Date', 'Time'), xscrollcommand=scroll_Bar_X.set, yscrollcommand=scroll_Bar_y.set)
scroll_Bar_X.config(command = student_Table.xview)
scroll_Bar_y.config(command=student_Table.yview)
# Columns of a Table
student_Table.heading('Id', text='ID')
student_Table.heading('Name', text='NAME')
student_Table.heading('Gender', text='GENDER')
student_Table.heading('Class', text='CLASS')
student_Table.heading('Mobile.No', text='MOBILE.NO')
student_Table.heading('Email-id', text='EMAIL-ID')
student_Table.heading('Address', text='ADDRESS')
student_Table.heading('Date', text='DATE')
student_Table.heading('Time', text='TIME')

student_Table.column('Id', width=50, anchor=CENTER)
student_Table.column('Name', width=300, anchor=CENTER)
student_Table.column('Gender', width=100, anchor=CENTER)
student_Table.column('Class', width=100, anchor=CENTER)
student_Table.column('Mobile.No', width=300, anchor=CENTER)
student_Table.column('Email-id', width=300, anchor=CENTER)
student_Table.column('Address', width=300, anchor=CENTER)
student_Table.column('Date', width=120, anchor=CENTER)
student_Table.column('Time', width=120, anchor=CENTER)


style =ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 12))
style.configure('Treeview.Heading', font=('arial', 14, 'bold'))
student_Table.config(show='headings')
student_Table.pack(fill=BOTH, expand=1)
root.mainloop()