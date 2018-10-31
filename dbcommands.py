import sqlite3
import sys

def insert_book(title, author, yr, isbn, price, stock=0):
  #Function to insert new books
  try:
     con= sqlite3.connect('bookstore.db')
     con.execute("INSERT INTO BOOKS(TITLE,AUTHOR,YEAR,ISBN,PRICE,STOCK) VALUES (?,?,?,?,?,?)",(title, author, yr, isbn, price, stock));
     con.commit()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise

def update_book(i,title, author, yr, isbn, price, stock):
  #Function to update book record
  try:
     con= sqlite3.connect('bookstore.db')
     con.execute("UPDATE BOOKS SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=?, PRICE=?,STOCK=? WHERE ID=?",(title, author, yr, isbn, price,stock, i));
     con.commit()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
    
def update_stock(i,new_stock):
  #Function to update book record
  try:
     con= sqlite3.connect('bookstore.db')
     con.execute("UPDATE BOOKS SET STOCK=? WHERE ID=?",(new_stock, i));
     con.commit()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
def delete_book(i):
  #Function to delete book record
  try:
     con= sqlite3.connect('bookstore.db')
     con.execute("DELETE FROM BOOKS WHERE ID=?",(i,));
     con.commit()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
    
def search_book(price, stock,tl="",auth="",yr="",isbn=""):
  #Function to search books
  searchbooks=[]
  try:
     con= sqlite3.connect('bookstore.db')
     cursor=con.cursor()
     cursor.execute("SELECT * FROM BOOKS WHERE TITLE LIKE ? AND AUTHOR LIKE ? AND YEAR LIKE ? OR ISBN=? OR PRICE=? OR STOCK=? COLLATE NOCASE",(tl,auth,yr,isbn,price,stock));
     searchbooks=cursor.fetchall()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
  return searchbooks

def search_book_order(price, stock,tl="",auth=""):
  #Function to search books for order
  searchbooks=[]
  try:
     con= sqlite3.connect('bookstore.db')
     cursor=con.cursor()
     cursor.execute("SELECT ID, TITLE, AUTHOR, PRICE, STOCK FROM BOOKS WHERE TITLE LIKE ? AND AUTHOR LIKE ? OR PRICE=? OR STOCK=? COLLATE NOCASE",(tl,auth,price,stock));
     searchbooks=cursor.fetchall()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
  return searchbooks

def select_all_books():
  #Function to search books
  allbooks=[]
  try:
     con= sqlite3.connect('bookstore.db')
     cursor=con.cursor()
     cursor.execute("SELECT * FROM BOOKS");
     allbooks=cursor.fetchall()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
  return allbooks

def get_books_to_order():
    #Function to search books
  orderbooks=[]
  try:
     con= sqlite3.connect('bookstore.db')
     cursor=con.cursor()
     cursor.execute("SELECT ID, TITLE, AUTHOR, PRICE, STOCK FROM BOOKS");
     orderbooks=cursor.fetchall()
     con.close()
  except:
     print("Exception:",sys.exc_info()[0])
     raise
  return orderbooks
