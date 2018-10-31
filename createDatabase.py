import sqlite3
import sys
from books import *

try:
  #create Database
  con= sqlite3.connect('bookstore.db')
  con.execute('''CREATE TABLE IF NOT EXISTS BOOKS(ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT, AUTHOR TEXT, YEAR TEXT, ISBN TEXT, PRICE REAL, STOCK INTEGER DEFAULT 0)''')
  con.commit()

  #import initial records:
  for items in booklist:
    con.execute("INSERT INTO BOOKS(TITLE,AUTHOR,YEAR,ISBN,PRICE,STOCK) VALUES (?,?,?,?,?,?)",items);
    con.commit()

  con.close()

except:
    print("Exception:",sys.exc_info()[0])
    raise
    
