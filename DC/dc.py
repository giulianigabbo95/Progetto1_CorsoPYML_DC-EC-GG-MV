import Elettrodomestico from gg

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


#MANCA IL RESTO DEL MAIN
# Nel menu, case "1" per aggiungere elettrodomestico:
case "3":
    print("Tipo alimentazione:")
    print("1. Elettrico")
    print("2. Gas")
    scelta_alim = input("Scegli (1/2): ")
    
    if scelta_alim == "1":
        alimentazione = "elettrico"
    elif scelta_alim == "2":
        alimentazione = "gas"
    else:
        pass
    
    scelta_ventilato = input("Ha funzione ventilata? (s/n): ").lower() == "s" # Torna True
    
'''
# Metodo altenativo 1 alla riga superiore:
    scelta_ventilato = input("Ha funzione ventilata? (s/n): ").lower()
    
    if scelta_ventilato == "s"
        ventilato = True
    elif scelta_ventilato == "n"
        ventilato == False
    else
        print("Inserimento non corretto. Imposto NON ventilato di default")
        ventilato = False
'''
'''
# Metodo altenativo 2 alla riga superiore:
    while True
        
        scelta_ventilato = input("Ha funzione ventilata? (s/n): ").lower()
        
        if scelta_ventilato == "s"
            ventilato = True
            break
        elif scelta_ventilato == "n"
            ventilato == False
            break
        else
            print("Inserimento non corretto. Riprova!")
'''

    forno_1 = Forno(marca, modello, anno, guasto, alimentazione, ventilato)
    officina.aggiungi_elettrodomestico(elettro)