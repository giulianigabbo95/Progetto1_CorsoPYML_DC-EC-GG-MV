import Elettrodomestico

class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato
    
    #getter & setter
    def getTipoAlimentazione(self):
        return self.__tipo_alimentazione
    
    def getHaVentilato(self):
        return self.__ha_ventilato
    
    def setTipoAlimentazione(self, tipo):
        self.__tipo_alimentazione = tipo
    
    def setHaVentilato(self, ha_ventilato):
        self.__ha_ventilato = ha_ventilato
    
    def stima_costo_base(self):
        costo = super().stima_costo_base()
        if self.__tipo_alimentazione == "gas":
            costo += 40
        if self.__ha_ventilato:
            costo += 15
        return costo