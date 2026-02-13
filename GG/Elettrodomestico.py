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