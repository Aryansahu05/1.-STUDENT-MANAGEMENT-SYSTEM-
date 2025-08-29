import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
import subprocess
import webbrowser
import os  # or webbrowser



#pymysql

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")


win.config(bg="brown")

title_label = tk.Label(win,text="Student Management System",font=("TIMES NEW ROMAN",30,"bold"),border=12,relief=tk.GROOVE,bg="pink",foreground="brown")
title_label.pack(side=tk.TOP,fill=tk.X)
detail_frame= tk.LabelFrame(win,text="Enter Details",font=("TIMES NEW ROMAN",20),bg="pink",fg="brown",border=12)
detail_frame.place(x=20,y=90,width=600,height=1100)

data_frame = tk.Frame(win,bd=12,bg="beige",relief=tk.GROOVE)
data_frame.place(x=640,y=90,width=880,height=630)



# Canvas to add scrolling functionality
canvas_frame = tk.Frame(win, bg="brown",border=6)  # A container frame for the canvasdata_frame = tk.Frame(win,bd=12,bg="pink",relief=tk.GROOVE)

canvas_frame.place(x=40, y=150, width=520, height=800)  # Adjust size to make scrolling necessary

# Create the canvas
canvas = tk.Canvas(canvas_frame, bg="beige", borderwidth=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add Vertical Scrollbar
y_scroll = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=y_scroll.set)

# Add detail_frame inside the canvas
detail_frame = tk.Frame(canvas, bg="beige")  # Frame to hold the input fields
canvas.create_window((0, 0), window=detail_frame, anchor="nw")  # Attach detail_frame to canvas

# Configure canvas scrolling region dynamically
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

detail_frame.bind("<Configure>", configure_canvas)

# Populate detail_frame with widgets to test scrolling
for i in range(32):  # Adding 50 rows of sample labels and entries
    label = tk.Label(detail_frame, text=f" {i + 1}", font=("TIMES NEW ROMAN", 15), fg="brown")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

    entry = tk.Entry(detail_frame, font=("TIMES NEW ROMAN", 15), bd=7)
    entry.grid(row=i, column=1, padx=5, pady=5)
    
    
#=================variables===================#
rollno = tk.StringVar()
name = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathersnm = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
branch = tk.StringVar()
language = tk.StringVar()
mothersnm = tk.StringVar()
religion = tk.StringVar()
adhar = tk.StringVar()
marital = tk.StringVar()
skills = tk.StringVar()
email = tk.StringVar()
boards= tk.StringVar()
schoolname = tk.StringVar()
examresult = tk.StringVar()
enrollment = tk.StringVar()
category = tk.StringVar()
fathersoccup = tk.StringVar()
courses = tk.StringVar()
statenm = tk.StringVar()





#======Entry========#

rollno_Ibl = tk.Label(detail_frame,text="Roll no",font=("TIMES NEW ROMAN",15),fg="brown")
rollno_Ibl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_Ibl = tk.Label(detail_frame,text="Name",font=("TIMES NEW ROMAN",15),fg="brown")
name_Ibl.grid(row=1,column=0,padx=2,pady=2)

name_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)
 
section_Ibl = tk.Label(detail_frame,text="Section",font=("TIMES NEW ROMAN",15),fg="brown")
section_Ibl.grid(row=2,column=0,padx=2,pady=2)

section_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=section)
section_ent.grid(row=2,column=1,padx=2,pady=2)

contact_Ibl = tk.Label(detail_frame,text="Contact no",font=("TIMES NEW ROMAN",15),fg="brown")
contact_Ibl.grid(row=3,column=0,padx=2,pady=2)

contact_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=contact)
contact_ent.grid(row=3,column=1,padx=2,pady=2)

father_Ibl = tk.Label(detail_frame,text="Fathers name",font=("TIMES NEW ROMAN",15),fg="brown")
father_Ibl.grid(row=4,column=0,padx=2,pady=2)

father_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=fathersnm)
father_ent.grid(row=4,column=1,padx=2,pady=2)

address_Ibl = tk.Label(detail_frame,text="Address",font=("TIMES NEW ROMAN",15),fg="brown")
address_Ibl.grid(row=5,column=0,padx=2,pady=2)

address_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=address)
address_ent.grid(row=5,column=1,padx=2,pady=2)

gender_Ibl = tk.Label(detail_frame,text="Gender",font=("TIMES NEW ROMAN",15),fg="brown")
gender_Ibl.grid(row=6,column=0,padx=2,pady=2)

gender_ent = ttk.Combobox(detail_frame,font=("TIMES NEW ROMAN",15),state="readonly",textvariable=gender)
gender_ent['values'] = ("male","female","others")
gender_ent.grid(row=6,column=1,padx=2,pady=2)

dob_Ibl = tk.Label(detail_frame,text="D.O.B.",font=("TIMES NEW ROMAN",15),fg="brown")
dob_Ibl.grid(row=7,column=0,padx=2,pady=2)

dob_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=dob)
dob_ent.grid(row=7,column=1,padx=2,pady=2)



branch_Ibl = tk.Label(detail_frame,text="Branch",font=("TIMES NEW ROMAN",15),fg="brown")
branch_Ibl.grid(row=8,column=0,padx=2,pady=2)

branch_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=branch)
branch_ent.grid(row=8,column=1,padx=2,pady=2)


language_Ibl = tk.Label(detail_frame,text="Language known",font=("TIMES NEW ROMAN",15),fg="brown")
language_Ibl.grid(row=9,column=0,padx=2,pady=2)

language_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=language)
language_ent.grid(row=9,column=1,padx=2,pady=2)

mom_Ibl = tk.Label(detail_frame,text="Mothers name",font=("TIMES NEW ROMAN",15),fg="brown")
mom_Ibl.grid(row=10,column=0,padx=2,pady=2)

mom_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=mothersnm)
mom_ent.grid(row=10,column=1,padx=2,pady=2)

religion_Ibl = tk.Label(detail_frame,text="Religion",font=("TIMES NEW ROMAN",15),fg="brown")
religion_Ibl.grid(row=11,column=0,padx=2,pady=2)

religion_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=religion)
religion_ent.grid(row=11,column=1,padx=2,pady=2)

Adhar_Ibl = tk.Label(detail_frame,text="Adhar no.",font=("TIMES NEW ROMAN",15),fg="brown")
Adhar_Ibl.grid(row=12,column=0,padx=2,pady=2)

Adhar_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=adhar)
Adhar_ent.grid(row=12,column=1,padx=2,pady=2)

marry_Ibl = tk.Label(detail_frame,text="Marital status",font=("TIMES NEW ROMAN",15),fg="brown")
marry_Ibl.grid(row=13,column=0,padx=2,pady=2)

marry_ent = ttk.Combobox(detail_frame,font=("TIMES NEW ROMAN",15),state="readonly",textvariable=marital)
marry_ent['values'] = ("Married","Unmarried")
marry_ent.grid(row=13,column=1,padx=2,pady=2)



skills_Ibl = tk.Label(detail_frame,text="Skills",font=("TIMES NEW ROMAN",15),fg="brown")
skills_Ibl.grid(row=14,column=0,padx=2,pady=2)

skills_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=skills)
skills_ent.grid(row=14,column=1,padx=2,pady=2)



email_Ibl = tk.Label(detail_frame,text="Email- id",font=("TIMES NEW ROMAN",15),fg="brown")
email_Ibl.grid(row=15,column=0,padx=2,pady=2)

email_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=email)
email_ent.grid(row=15,column=1,padx=2,pady=2)

board_Ibl = tk.Label(detail_frame,text="12 board year and percentage",font=("TIMES NEW ROMAN",15),fg="brown")
board_Ibl.grid(row=16,column=0,padx=2,pady=2)

board_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=boards)
board_ent.grid(row=16,column=1,padx=2,pady=2)

exam_Ibl = tk.Label(detail_frame,text="10 board year and percentage",font=("TIMES NEW ROMAN",15),fg="brown")
exam_Ibl.grid(row=17,column=0,padx=2,pady=2)

exam_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=examresult)
exam_ent.grid(row=17,column=1,padx=2,pady=2)

school_Ibl = tk.Label(detail_frame,text="School name",font=("TIMES NEW ROMAN",15),fg="brown")
school_Ibl.grid(row=18,column=0,padx=2,pady=2)

school_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=schoolname)
school_ent.grid(row=18,column=1,padx=2,pady=2)

enrol_Ibl = tk.Label(detail_frame,text="Enrollment no.",font=("TIMES NEW ROMAN",15),fg="brown")
enrol_Ibl.grid(row=19,column=0,padx=2,pady=2)

enrol_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=enrollment)
enrol_ent.grid(row=19,column=1,padx=2,pady=2)

category_Ibl = tk.Label(detail_frame,text="category",font=("TIMES NEW ROMAN",15),fg="brown")
category_Ibl.grid(row=20,column=0,padx=2,pady=2)

category_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=category)
category_ent.grid(row=20,column=1,padx=2,pady=2)

occup_Ibl = tk.Label(detail_frame,text="fathers occupation",font=("TIMES NEW ROMAN",15),fg="brown")
occup_Ibl.grid(row=21,column=0,padx=2,pady=2)

occup_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=fathersoccup)
occup_ent.grid(row=21,column=1,padx=2,pady=2)

course_Ibl = tk.Label(detail_frame,text="Course Name",font=("TIMES NEW ROMAN",15),fg="brown")
course_Ibl.grid(row=22,column=0,padx=2,pady=2)

course_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=courses)
course_ent.grid(row=22,column=1,padx=2,pady=2)

state_Ibl = tk.Label(detail_frame,text="State",font=("TIMES NEW ROMAN",15),fg="brown")
state_Ibl.grid(row=23,column=0,padx=2,pady=2)

state_ent = tk.Entry(detail_frame,bd=7,font=("TIMES NEW ROMAN",15),textvariable=statenm)
state_ent.grid(row=23,column=1,padx=2,pady=2)


#========================#



#========functions========#
def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * From  data")
    rows = curr.fetchall()
    if len(rows)!=0:
       student_table.delete( *student_table.get_children())
       for row in rows:
           student_table.insert('',tk.END,values=row)
    conn.commit()
    conn.close()   

       
       
def add_func():
    if rollno.get()=="" or name.get()=="" or section.get()==""or contact.get()=="" or fathersnm.get()=="" or address.get()=="" or gender.get()==""or dob.get()==""or branch.get()=="" or language.get()==""or mothersnm.get()=="" or religion.get()=="" or adhar.get()=="" or marital.get()=="" or skills.get()=="" or email.get()=="" or boards.get()=="" or schoolname.get()=="" or examresult.get()=="" or enrollment.get()=="" or category.get()=="" or fathersoccup.get()=="" or courses.get()=="" or statenm.get()=="" :
        messagebox.showerror("Error!","please fill all the fields!")
    else:
        conn = pymysql.connect(host= "localhost" ,user ="root", password = "" , database ="sms1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(), name.get(), section.get(), contact.get(), fathersnm.get(), address.get(), gender.get(), dob.get(), branch.get(), language.get(), mothersnm.get() ,religion.get(), adhar.get(), marital.get(), skills.get(), email.get(), boards.get(), schoolname.get(), examresult.get(), enrollment.get(), category.get(), fathersoccup.get(), courses.get(), statenm.get()))
        conn.commit()
        conn.close()
        
        fetch_data()

def get_cursor(event):
    '''this function fetch data of the selected row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    section.set(row[2])
    contact.set(row[3])
    fathersnm.set(row[4])
    address.set(row[5])
    gender.set(row[6])
    dob.set(row[7])
    branch.set(row[8]) 
    language.set(row[9])
    mothersnm.set(row[10])
    religion.set(row[11])
    adhar.set(row[12])
    marital.set(row[13])
    skills.set(row[14]) 
    email.set(row[15])
    examresult.set(row[16])
    boards.set(row[17])
    schoolname.set(row[18])
    enrollment.set(row[19])
    category.set(row[20])
    fathersoccup.set(row[21])
    courses.set(row[22])
    statenm.set(row[23])
    
    
    
    
def clear_func():
    '''this function will clear everything'''
    rollno.set("")
    name.set("")
    section.set("")
    contact.set("")
    fathersnm.set("")
    address.set("")
    gender.set("")
    dob.set("")
    branch.set("") 
    language.set("")
    mothersnm.set("")
    religion.set("")
    adhar.set("")
    marital.set("")
    skills.set("") 
    email.set("")
    examresult.set("")
    boards.set("")
    schoolname.set("")
    enrollment.set("")
    category.set("")
    fathersoccup.set("")
    courses.set("")
    statenm.set("")
    
    
    



def update_func():
    conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
    curr = conn.cursor()
    curr.execute("""
        UPDATE data SET 
            `Name`=%s, 
            `Section`=%s,
            `Contact`=%s, 
            `Fathers Name`=%s, 
            `Address`=%s, 
            `Gender`=%s, 
            `D.O.B.`=%s,
            `branch`=%s,
            `language known`=%s,
            `mothersname`=%s,
            `religion`=%s,
            `adharno.`=%s,
            `marital status`=%s,
            `skills`=%s,
            `e mail`=%s,
            `boards`=%s,
            `exam result`=%s,
            `schoolname`=%s,
            `enrollment`=%s,
            `category`=%s,
            `fathers occupation`=%s,
            `courses`=%s,
            `statename`=%s
        WHERE `Roll No.`=%s
    """, (
        name.get(), section.get(), contact.get(), fathersnm.get(), address.get(), gender.get(), dob.get(),
        branch.get(), language.get(), mothersnm.get(), religion.get(), adhar.get(), marital.get(), skills.get(),
        email.get(), boards.get(), examresult.get(), schoolname.get(), enrollment.get(), category.get(),
        fathersoccup.get(), courses.get(), statenm.get(), rollno.get()
    ))
    conn.commit()
    conn.close()
    fetch_data()
    clear_func()
    messagebox.showinfo("Success", "Record updated successfully.")


def delete_func():
    selected_item = student_table.focus()
    if not selected_item:
        messagebox.showwarning("No selection", "Please select a student to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
    if confirm:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("DELETE FROM data WHERE rollno = %s", (rollno.get(),))
            conn.commit()
            conn.close()
            fetch_data()
            clear_func()
            messagebox.showinfo("Success", "Record deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

def open_predictor():
   
    subprocess.Popen(["python", os.path.join("C:/Users/aryan/Downloads/placement_predictor", "app.py")])

    webbrowser.open("http://127.0.0.1:5000")


                       

#=================================#

#====buttons=============#

btn_frame = tk.Frame(detail_frame,bg="brown",bd=10,relief=tk.GROOVE)
btn_frame.place(x=8,y=1200,width=460,height=220)

add_btn = tk.Button(btn_frame,bg="brown",text="ADD",bd=7,font=("TIMES NEW ROMAN",17),width=15,command=add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="brown",text="Update",bd=7,font=("TIMES NEW ROMAN",17),width=15,command=update_func)
update_btn.grid(row=0,column=1,padx=3,pady=2)

delete_btn = tk.Button(btn_frame,bg="brown",text="Delete",bd=7,font=("TIMES NEW ROMAN",17),width=15,command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="brown",text="Clear",bd=7,font=("TIMES NEW ROMAN",17),width=15,command=clear_func)
clear_btn.grid(row=1,column=1,padx=3,pady=2)

placement_btn = tk.Button(
    btn_frame,
    text="Placement Predictor",
    bg="brown",
    bd=7,
    font=("TIMES NEW ROMAN", 17),
    width=32,
    command=open_predictor
)
placement_btn.grid(row=2, column=0, columnspan=2, padx=2, pady=5)


#===========================#


#========database frame======#

y_scroll = tk.Scrollbar(data_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(data_frame, orient=tk.HORIZONTAL)

columns = ("Roll No.", "Name",  "Section", "Contact", "Fathers Name", "Address", "Gender", "D.O.B.","branch","language known","mothersname","religion","adharno.","marital status","skills","e mail","boards","exam result","schoolname","enrollment","category","fathers occupation","courses","statename")

student_table = ttk.Treeview(
    data_frame,
    columns=columns,
    yscrollcommand=y_scroll.set,
    xscrollcommand=x_scroll.set
)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

# Set headings
for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table['show'] = 'headings'

student_table.pack(fill=tk.BOTH, expand=True)

fetch_data()


student_table.bind("<ButtonRelease-1>",get_cursor)
#===========================================#


win.mainloop()
            