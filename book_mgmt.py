from tkinter import *
import tkinter.messagebox as mbox
from dbcommands import *
from billing import *

def login_check():
    global loginsuccess,rootlogin
    username=uname.get()
    password = passwd.get()
    
    if (username == 'admin' and  password == 'admin'):
        mbox.showinfo('info','Logged in Successfully')
        loginsuccess='yes'
        rootlogin.destroy()
    else:
        mbox.showinfo('Error','Invalid username/password. Please try again')
        loginsuccess='no'

def login():
    #global variable declaration
    global  uname, passwd, loginsuccess, rootlogin
    rootlogin = Tk()
    rootlogin.title("Bookstore")
    frame=Frame(rootlogin)

    uname_lbl = Label(rootlogin, text = 'Username:')
    uname_lbl.pack(padx=15,pady= 5)

    uname = Entry(rootlogin,bd =5)
    uname.pack(padx=15, pady=5)

    passwd_lbl = Label(rootlogin, text = 'Password: ')
    passwd_lbl.pack(padx = 15,pady=6)

    passwd = Entry(rootlogin,show="*", bd=5)
    passwd.pack(padx = 15,pady=7)

    login_btn = Button(frame, text = 'Login',command = login_check)

    login_btn.pack(side = RIGHT , padx =5)
    frame.pack(padx=100,pady = 19)



    
def get_selected(event):
    global selected
    global entry1,entry2,entry3,entry4,entry5,entry6
    index=booklist.curselection()[0]
    selected=booklist.get(index)
    #fill the textboxes with selected values
    entry1.delete(0,END)
    entry1.insert(END,selected[1])
    entry2.delete(0,END)
    entry2.insert(END,selected[2])
    entry3.delete(0,END)
    entry3.insert(END,selected[3])
    entry4.delete(0,END)
    entry4.insert(END,selected[4])
    entry5.delete(0,END)
    entry5.insert(END,selected[5])
    entry6.delete(0,END)
    entry6.insert(END,selected[6])
    
def get_all_books():
    booklist.delete(0,END)
    for r in select_all_books():
        booklist.insert(END,r)

def add_book_command():
    insert_book(title_textbox.get(),author_textbox.get(),year_textbox.get(),isbn_textbox.get(),price_textbox.get(),stock_textbox.get())
    get_all_books()
    print("added=",title_textbox.get(),author_textbox.get(),year_textbox.get(),isbn_textbox.get(),price_textbox.get(),stock_textbox.get())

def delete_book_command():
    delete_book(selected[0])
    print("deleted=",selected[0])
    get_all_books()

def search_book_command():
    booklist.delete(0,END)
    for r in search_book(price_textbox.get(),stock_textbox.get(),"%"+title_textbox.get()+"%","%"+author_textbox.get()+"%","%"+year_textbox.get()+"%",isbn_textbox.get()):
        booklist.insert(END,r)

def update_book_command():
    update_book(selected[0],title_textbox.get(),author_textbox.get(),year_textbox.get(),isbn_textbox.get(),price_textbox.get(),stock_textbox.get())
    get_all_books()
    print("updated=",selected[0])

def generate_bill_command():
    billtk=generate_bill()
    
def reset_entries():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')

def book_mgmt():
    global title_textbox, author_textbox, year_textbox, isbn_textbox, price_textbox, stock_textbox
    global entry1, entry2, entry3, entry4, entry5, entry6
    global booklist

    root = Tk()
    root.title("Book Store Management")
    
    frame1 = Frame(root)
    frame1.pack()

    label1=Label(frame1,text="Title")
    label1.grid(row=0,column=0)

    label2=Label(frame1,text="Author")
    label2.grid(row=0,column=2)

    label3=Label(frame1,text="Year")
    label3.grid(row=1,column=0)

    label4=Label(frame1,text="ISBN")
    label4.grid(row=1,column=2)
    
    label5=Label(frame1,text="Price")
    label5.grid(row=0,column=4)

    label6=Label(frame1,text="Stock Qty")
    label6.grid(row=1,column=4)
    
    title_textbox=StringVar()
    entry1=Entry(frame1,textvariable=title_textbox)
    entry1.grid(row=0,column=1)

    author_textbox=StringVar()
    entry2=Entry(frame1,textvariable=author_textbox)
    entry2.grid(row=0,column=3)

    year_textbox=StringVar()
    entry3=Entry(frame1,textvariable=year_textbox)
    entry3.grid(row=1,column=1)

    isbn_textbox=StringVar()
    entry4=Entry(frame1,textvariable=isbn_textbox)
    entry4.grid(row=1,column=3)

    price_textbox=StringVar()
    entry5=Entry(frame1,textvariable=price_textbox)
    entry5.grid(row=0,column=5)

    stock_textbox=StringVar()
    entry6=Entry(frame1,textvariable=stock_textbox)
    entry6.grid(row=1,column=5)
    
    booklist=Listbox(frame1, height=7,width=36)
    booklist.grid(row=2,column=0,rowspan=7,columnspan=2)

    scorllbar1=Scrollbar(frame1)
    scorllbar1.grid(row=2,column=2,rowspan=7)

    booklist.configure(yscrollcommand=scorllbar1.set)
    scorllbar1.configure(command=booklist.yview)

    booklist.bind('<<ListboxSelect>>',get_selected)

    rstBtn=Button(frame1,text="Reset Entries", width=12,command=reset_entries)
    rstBtn.grid(row=2,column=3)

    billBtn=Button(frame1,text="Billing", width=12,command=generate_bill_command)
    billBtn.grid(row=2,column=4)
    
    btn1=Button(frame1,text="View all", width=12,command=get_all_books)
    btn1.grid(row=3,column=3)

    btn2=Button(frame1,text="Search Book", width=12,command=search_book_command)
    btn2.grid(row=4,column=3)

    btn3=Button(frame1,text="Add Book", width=12,command=add_book_command)
    btn3.grid(row=5,column=3)

    btn4=Button(frame1,text="Update selected", width=12,command=update_book_command)
    btn4.grid(row=6,column=3)

    btn5=Button(frame1,text="Delete selected", width=12,command=delete_book_command)
    btn5.grid(row=7,column=3)

    btn6=Button(frame1,text="Close", width=12,command=root.destroy)
    btn6.grid(row=8,column=3)

    return root    
#######################

##########################

loginsuccess = 'no'

login()

rootlogin.mainloop()

if(loginsuccess=='yes'):
    root=book_mgmt()
    root.mainloop()


#####################

