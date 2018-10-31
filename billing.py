from tkinter import *
import tkinter.messagebox as mbox
from dbcommands import *
from invoice_generator import *

def generate_bill():
    #Function to generate bills
    global BLtitle_textbox, BLauthor_textbox, BLprice_textbox, BLstock_textbox, BLorder_qty_textbox, BLlabel_showtotal, BLlabel_tax, BLlabel_shownettotal
    global BLentry1, BLentry2, BLentry3, BLentry4, BLentry5
    global BLbookorderlist, bookorderlist
    global Total, Tax, NetTotal

    Total=0.0
    Tax=0.0
    NetTotal=0.0

    BL = Tk()
    BL.title("Billing")
    BLframe=Frame(BL)
    BLframe.pack()

    BLlabel1=Label(BLframe,text="Title")
    BLlabel1.grid(row=0,column=0)

    BLlabel2=Label(BLframe,text="Author")
    BLlabel2.grid(row=0,column=2)
    
    BLlabel3=Label(BLframe,text="Price")
    BLlabel3.grid(row=0,column=4)

    BLlabel4=Label(BLframe,text="Stock Qty")
    BLlabel4.grid(row=1,column=4)

    BLlabel5=Label(BLframe,text="Order Qty")
    BLlabel5.grid(row=2,column=4)
    
    BLtitle_textbox=StringVar()
    BLentry1=Entry(BLframe,textvariable=BLtitle_textbox)
    BLentry1.grid(row=0,column=1)

    BLauthor_textbox=StringVar()
    BLentry2=Entry(BLframe,textvariable=BLauthor_textbox)
    BLentry2.grid(row=0,column=3)

    BLprice_textbox=StringVar()
    BLentry3=Entry(BLframe,textvariable=BLprice_textbox)
    BLentry3.grid(row=0,column=5)

    BLstock_textbox=StringVar()
    BLentry4=Entry(BLframe,textvariable=BLstock_textbox)
    BLentry4.grid(row=1,column=5)

    BLorder_qty_textbox=StringVar()
    BLentry5=Entry(BLframe,textvariable=BLorder_qty_textbox)
    BLentry5.grid(row=2,column=5)
    
    bookorderlist=Listbox(BLframe, height=7,width=36)
    bookorderlist.grid(row=2,column=0,rowspan=7,columnspan=2)

    scorllbar1=Scrollbar(BLframe)
    scorllbar1.grid(row=2,column=2,rowspan=7)

    bookorderlist.configure(yscrollcommand=scorllbar1.set)
    scorllbar1.configure(command=bookorderlist.yview)

    bookorderlist.bind('<<ListboxSelect>>',get_selected_book)

    BLbookorderlist=Listbox(BLframe, height=7,width=36)
    BLbookorderlist.grid(row=2,column=10,rowspan=7,columnspan=2)

    scorllbar2=Scrollbar(BLframe)
    scorllbar2.grid(row=2,column=12,rowspan=7)

    BLbookorderlist.configure(yscrollcommand=scorllbar2.set)
    scorllbar2.configure(command=BLbookorderlist.yview)

    BLbtn1=Button(BLframe,text="View all", width=12,command=get_booksorder)
    BLbtn1.grid(row=3,column=3)
    
    BLbtn1=Button(BLframe,text="Search Book", width=12,command=search_book_to_order)
    BLbtn1.grid(row=4,column=3)

    BLbtn2=Button(BLframe,text="Add to Order", width=12,command=add_to_order)
    BLbtn2.grid(row=5,column=3)

    BLbtn4=Button(BLframe,text="Close", width=12,command=BL.destroy)
    BLbtn4.grid(row=16,column=3)
    
    BLbtn5=Button(BLframe,text="Generate Invoice", width=12,command=invoice_command)
    BLbtn5.grid(row=14,column=3)
    
    BLlabel_total=Label(BLframe,text="Total")
    BLlabel_total.grid(row=10,column=6)

    BLlabel_showtotal=Label(BLframe,text="0.0")
    BLlabel_showtotal.grid(row=10,column=8)

    BLlabel_ltax=Label(BLframe,text="Tax Total")
    BLlabel_ltax.grid(row=11,column=6)

    BLlabel_tax=Label(BLframe,text="0.0")
    BLlabel_tax.grid(row=11,column=8)
    
    BLlabel_nettotal=Label(BLframe,text="Net Total(incl. tax)")
    BLlabel_nettotal.grid(row=12,column=6)

    BLlabel_shownettotal=Label(BLframe,text="0.0")
    BLlabel_shownettotal.grid(row=12,column=8)

    return BL

def invoice_command():
    #call invoice generator function to create invoice pdf
    generate_invoice(BLbookorderlist, Total, Tax, NetTotal)

def get_booksorder():
    bookorderlist.delete(0,END)
    for r in get_books_to_order():
        bookorderlist.insert(END,r)
        
    print("bookorderlist:",bookorderlist.get(0,END))
        
def get_selected_book(event):
    global selected_book
    global BLentry1, BLentry2, BLentry3, BLentry4
    index=bookorderlist.curselection()[0]
    selected_book=bookorderlist.get(index)
    #fill the textboxes with selected values
    BLentry1.delete(0,END)
    BLentry1.insert(END,selected_book[1])
    BLentry2.delete(0,END)
    BLentry2.insert(END,selected_book[2])
    BLentry3.delete(0,END)
    BLentry3.insert(END,selected_book[3])
    BLentry4.delete(0,END)
    BLentry4.insert(END,selected_book[4])

    print("BLentries:",BLentry1.get(),BLentry2.get(),BLentry3.get(),BLentry4.get())

def search_book_to_order():
    bookorderlist.delete(0,END)
    for r in search_book_order(BLentry3.get(),BLentry4.get(),"%"+BLentry1.get()+"%","%"+BLentry2.get()+"%"):
        bookorderlist.insert(END,r)

def add_to_order():
    global BLbookorderlist, BLlabel_showtotal, BLlabel_shownettotal, Total, Tax, NetTotal
    
    t=[selected_book[0],BLentry1.get(),BLentry2.get(),BLentry3.get(),BLentry5.get()]
    
    print("Add to order:",t)
    print("selected_book:",selected_book)

    new_stock=(int)(BLentry4.get())-(int)(BLentry5.get())

    BLbookorderlist.insert(END,t)

    Price=(float)(BLentry3.get())
    Quantity=(float)(BLentry5.get())

    #Update stock
    update_stock(selected_book[0],new_stock)
    #update the displayed list
    get_booksorder()
    #calculate Total
    Total+= Price * Quantity
    
    Tstring=str('%.2f'%(Total))
    tax=0.05*Total
    NetTotal=tax+Total
    Taxstring=str('%.2f'%(tax))
    NTstring=str('%.2f'%(NetTotal))
    BLlabel_showtotal.configure(text=Tstring)
    BLlabel_tax.configure(text=Taxstring)
    BLlabel_shownettotal.configure(text=NTstring)
    

    
