'''
Esercizio: Gestionale Officina Elettrodomestici
Progettare un sistema a oggetti per un'officina che ripara elettrodomestici.
Il programma deve modellare elettrodomestici, ticket di riparazione e operazioni dell'officina utilizzando incapsulamento, ereditarietà, polimorfismo, type() e metodi variatici (*args, **kwargs).

Classe base: Elettrodomestico:
    Attributi privati (__ doppio underscore):
        - __marca (stringa)
        - __modello (stringa)
        - __anno_acquisto (intero)
        - __guasto (stringa)
    Metodi:
        - __init__(self, marca, modello, anno_acquisto, guasto): costruttore
        - descrizione(self): restituisce stringa con marca, modello, anno, guasto
        - stima_costo_base(self): restituisce un valore numerico (costo base diagnosi)
        - Getter e setter per tutti gli attributi (controllo: anno non può essere nel futuro)

    Regola 1 - Incapsulamento: attributi privati (__), accessibili solo tramite getter/setter.
'''

import datetime

class Elettrodomestico:
    def __init__(self, marca, modello, anno_acquisto, guasto):
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto
        
    def descriviElettrodomestico(self):
        print("L'elettrodomestico", self.__modello, "della marca", self.__marca, "acquistato nel", self.__anno_acquisto, "si è rotto per il guasto:", self.__guasto)
        
    def stimaCostoBase(self):
        costo_diagnosi = 50
        print("Il costo della diagnosi è:", costo_diagnosi)
        return costo_diagnosi
    
    def get_marca(self):
        return self.__marca
    def get_modello(self):
        return self.__modello
    def get_anno_acquisto(self):
        return self.__anno_acquisto
    def get_guasto(self):
        return self.__guasto
    
    def set_marca(self, marca):
        self.__marca = marca
    def set_modello(self, modello):
        self.__modello = modello
    def set_anno_acquisto(self, anno_acquisto):
        if anno_acquisto > datetime.now().year:
            print("Marty sei tu? Ritorno al Futuro!")
        else:
            self.__anno_acquisto = anno_acquisto
        
    def set_guasto(self, guasto):
        self.__guasto = guasto
    