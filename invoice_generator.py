import time
from random import randint
from reportlab.pdfgen import canvas

def generate_invoice(orderlist, total, tax, nettotal):
    #invoice generator function:
    filename="Invoice_%d"%randint(1,100000)+".pdf"
    c = canvas.Canvas(filename)
    
    time_value=time.strftime("%H:%M:%S")
    date_value=time.strftime("%m/%d/%Y")

    c.setLineWidth(.3)
    c.setFont('Helvetica', 15)
    c.line(50, 747, 580, 747) #FROM TOP 1ST LINE
    c.drawString(280, 750,"INVOICE")
    c.setFont('Helvetica', 12)
    c.drawString(60, 720, "BOOK STORE:- HOUSE OF BOOKS, IIT Branch")
    c.drawString(60, 690, "STORE ADDRESS: 3201 S. State Street")
    c.drawString(170, 660, "Chicago, IL 60616")
    c.drawString(450, 720, "DATE :- "+ date_value)
    c.drawString(450, 690, "TIME :- "+ time_value)
    c.line(450, 710, 560, 710)
    c.line(50, 640, 580, 640)#FROM TOP 2ST LINE
    c.line(50, 748, 50, 50)#LEFT LINE
    c.line(400, 640, 400, 50)# MIDDLE LINE
    c.line(580, 748, 580, 50)# RIGHT LINE
    c.drawString(475, 615, 'PRICE')
    c.drawString(100, 615, 'BOOK TITLE')
    c.line(50, 600, 580, 600)#FROM TOP 3rd LINE

    x=550
    for tlist in orderlist:
        for item in tlist:
           title=item[1]
           print("item[1]",item[1])
           c.drawString(60, x, title)
           print("item %s %s",item[3],item[4])
           price=float(item[3])
           qty=float(item[4])
           result=price*qty
           c.drawString(500, x,str(result))
           x-=30
        
    #TOTAL = int(amountpdf) * ((int(staxpdf)) / 100)
    c.drawString(60, 110, "TAX : %.2f"%tax)
    #c.drawString(500, 500, str("--TOTAL"))
    c.line(50, 100, 580, 100)#FROM TOP 4th LINE
    c.drawString(60, 80, "TOTAL AMOUNT : ")
    c.drawString(500, 80, str(nettotal))
    c.line(50, 50, 580, 50)#FROM TOP LAST LINE
    c.save()



booklist=[['The Fallen', 'David Baldacci',15.50,5], ['Gray Mountain', 'John Grisham',20.60,7], ['The Black Widow', 'Daniel Silva',10.25,10]]
total=23.32
tax=5.34
nettotal=34.54
#generate_invoice(booklist,total, tax, nettotal)

