class TicketRiparazione:

    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"
        self.__note = []


    def aggiungiNota(self, testo):
        self.__note.append(testo)

    def calcolaPreventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stimaCostoBase()
        for costo in voci_extra:
            totale += costo
        print(totale)
        return totale


    def get_id(self):
        return self.__id_ticket
    def get_elettrodomestico(self):
        return self.__elettrodomestico
    def get_stato(self):
        return self.__stato
    def get_note(self):
        return self.__note.copy()

    def set_stato(self, nuovo_stato):
        stati_validi = ["aperto", "in lavorazione", "chiuso"]
        if nuovo_stato.lower() in stati_validi:
            self.__stato = nuovo_stato.lower()
        else:
            print("Errore: Stato", nuovo_stato, "non valido!")