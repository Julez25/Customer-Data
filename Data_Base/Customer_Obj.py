import random
class NewCust():
    
    def __init__(self, id_Num_, id_Order_, first_Name_, sec_Name_, land_, region_, city_, plz_, adress_, auftrag_):
        self.id_Num_ = id_Num_
        self.id_Order_ = id_Order_
        self.first_Name_ = first_Name_
        self.sec_Name_ = sec_Name_
        self.land_ = land_
        self.region_ = region_
        self.city_ = city_
        self.plz = plz_
        self.adress_ = adress_
        self.auftrag_ = auftrag_
    
    def get_Id_num(self):
        return self.id_Num_
    def get_Id_Order(self):
        return self.id_Order_
    def get_First_Name(self):
        return self.first_Name_
    def get_Sec_Name(self):
        return self.sec_Name_
    def get_Land(self):
        return self.land_
    def get_Region(self):
        return self.region_
    def get_City(self):
        return self.city_
    def get_PLZ(self):
        return self.plz
    def get_Adress(self):
        return self.adress_
    




