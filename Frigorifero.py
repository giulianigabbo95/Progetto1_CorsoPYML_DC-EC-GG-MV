import Elettrodomestico

class Frigorifero(Elettrodomestico):

    def __init__(self, litri, ha_freezer):
        super().__init__()
        self.litri = litri
        self.ha_freezer = ha_freezer


    def stimaCostoBase(self):
        costo = 35
        if self.litri > 300:
            costo += 25
        if self.ha_freezer:
            costo += 15
        return costo

'''
    def get_litri(self):
        return self.__litri
    def get_ha_freezer(self):
        return self.__ha_freezer

    def set_litri(self, litri):
        self.__litri = litri
    def set_ha_freezer(self, ha_freezer):
        self.__ha_freezer = ha_freezer
'''