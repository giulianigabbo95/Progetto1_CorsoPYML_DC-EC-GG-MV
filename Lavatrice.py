from Elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):

    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga


    def stimaCostoBase(self):
        costo = super().stimaCostoBase()
        if self.capacita_kg > 8:
            costo += 30
        if self.giri_centrifuga > 1400:
            costo += 20
        return costo    

'''
    def get_capacita(self):
        return self.__capacita_kg
    def get_giri(self):
        return self.__giri_centrifuga

    def set_capacita(self, capacita):
        self.__capacita_kg = capacita
    def set_giri(self, giri):
        self.__giri_centrifuga = giri
'''