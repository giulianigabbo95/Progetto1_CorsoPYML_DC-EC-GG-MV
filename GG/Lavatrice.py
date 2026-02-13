import Elettrodomestico
        
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga
    
    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.__capacita_kg > 8:
            costo += 30
        if self.__giri_centrifuga > 1400:
            costo += 20
        return costo    
    
    def get_capacita(self):
        return self.__capacita_kg
    def get_giri(self):
        return self.__giri_centrifuga
    def set_capacita(self, capacita):
        self.__capacita_kg = capacita
    def set_giri(self, giri):
        self.__giri_centrifuga = giri
    
    
