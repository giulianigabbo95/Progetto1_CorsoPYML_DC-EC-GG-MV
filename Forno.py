import Elettrodomestico

class Forno(Elettrodomestico):

    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione
        # self.tipo_alimentazione = self._scegliAlimentazione(tipo_alimentazione)  # DA CHIEDERE A MIRKO
        self.ha_ventilato = ha_ventilato


    def stimaCostoBase(self):
        costo = super().stima_costo_base()
        if self.tipo_alimentazione == "gas":
                costo += 40
        if self.ha_ventilato == True:
            costo += 15
        return costo

'''
    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione
    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def set_tipo_alimentazione(self, tipo):
        self.__tipo_alimentazione = tipo
    def set_ha_ventilato(self, ha_ventilato):
        self.__ha_ventilato = ha_ventilato
'''