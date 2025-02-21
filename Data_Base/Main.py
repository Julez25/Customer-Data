import sqlite3
import Customer_Obj

#Daten durch die NewCust Class in die DataBase einfügen
def saveCust():
    cursor.execute("""
    INSERT INTO Users (
    id, 
    order_id, 
    first_N, 
    second_N, 
    land, 
    region, 
    city, 
    plz, 
    adress) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
    (newCust.get_Id_Num(),
     newCust.get_Id_Order(),
     newCust.get_First_Name(),
     newCust.get_Sec_Name(),
     newCust.get_Land(),
     newCust.get_Region(),
     newCust.get_City(),
     newCust.get_PLZ(),
     newCust.get_Adress())
     )
    conn.commit()

def getData():
    cursor.execute("SELECT * FROM Users")
    rows = cursor.fetchall()  # Holt alle Ergebnisse aus der Abfrage

    for row in rows:
        print(row)
#Verbindung zur Datenbank herstellen
conn = sqlite3.connect("Cust_Database.db") 
cursor = conn.cursor() #Cursor Objekt

#Tabelle mit Kundendaten erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER,
    order_id INTEGER,
    first_N TEXT NOT NULL,
    second_N TEXT NOT NULL,
    land TEXT NOT NULL,
    region TEXT NOT NULL,
    city TEXT NOT NULL,
    plz INTEGER,               
    adress TEXT NOT NULL    
)
""")
conn.commit()

newCust = Customer_Obj.NewCust(123, 200, "julian", "T", "DE", "By", "MU", 80689, "blabla")
saveCust()
getData()
cursor.close()
conn.close()

    


