import csv
class NewCust():
    
    def __init__(self, vorname_, nachname_, adresse_, auftrag_):
        self.vorname_ = vorname_
        self.nachname_ = nachname_
        self.adresse_ = adresse_
        self.auftrag_ = auftrag_
    
    def saveData(self):
        with open("Customer_List.csv", mode="w", newline="", encoding="utf-8") as file:
            dict_Data = {'Vorname ',
                     'Nachname ', 
                     'Adresse ',
                     'Auftrag '}
            saver_ = csv.writer(file)
            saver_.writerow(dict_Data)
    
    def getData(self):
        with open("Customer_List.csv", mode="r", newline="", encoding="utf-8") as file:
            getter_ = csv.reader(file)
            for row in getter_:
                print(row)
CustObj = NewCust("julian", "T", "blabalbla", "quitsche ente")
CustObj.saveData()
CustObj.getData()

