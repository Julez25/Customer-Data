import sqlite3
import Customer_Obj

#Verbindung zur Datenbank herstellen
conn = sqlite3.connect("Cust_Database.db") 
cursor = conn.cursor() #Cursor Objekt

#Tabelle mit Kundendaten erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER
    first_N TEXT NOT NULL,
    second_N TEXT NOT NULL,
    land TEXT NOT NULL,
    region TEXT NOT NULL,
    city TEXT NOT NULL,
    plz INTEGER,
    adress TEXT NOT NULL,
    
)
""")
conn.commit()

#Daten durch die Customer Class in die DataBase einfügen
def saveCust(Customer_):
    cursor.execute("INSERT INTO users (id, order_id, first_N, second_N, land, region, city, plz, adress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", ())
    
newCust = Customer_Obj()
saveCust(newCust)

