from Lavatrice import Lavatrice
from Frigorifero import Frigorifero
from Forno import Forno
from TicketRiparazione import TicketRiparazione

class Officina:

    def __init__(self, nome):
        self.nome = nome
        self.__tickets = []
        self.__elettrodomestici = []
        self.servizi_aggiuntivi = { 
            "Ritiro a Domicilio" : 20,
            "Consegna Rapida" : 15,
            "Ricambi Originali" : 50,
            "Pulizia Approfondita" : 10
        }


    def aggiungiElettrodomestico(self, elettrodomestico):
        self.__elettrodomestici.append(elettrodomestico)
        print(elettrodomestico.descriviElettrodomestico())
        elettrodomestico.descriviElettrodomestico()
        print("Aggiunto Elettrodomestico:", elettrodomestico.get_marca, elettrodomestico.get_modello)

    def aggiungiTicket(self, ticket):
        if type(ticket) == TicketRiparazione:
            self.__tickets.append(ticket)
            print("Ticket", ticket.get_id(), "aggiunto con successo.")
        else:
            print("Errore: Oggetto di Tipo non valido.")

    def chiudiTicket(self, id_ticket):
        for ticket in self.__tickets:
            if ticket.get_id() == id_ticket:
                ticket.setStato("chiuso")
                print("Ticket chiuso.")
                return
        print("Ticket non trovato.")

    def stampaTicketAperti(self):
        for ticket in self.__tickets:
            if ticket.getStato() != "chiuso":
                elettro = ticket.get_elettrodomestico()
                print("ID:", ticket.getId(), "| Tipo:", type(elettro).__name__, "| Stato:", ticket.getStato())

    def calcolaTotalePreventivo(self):
        totale = 0
        for ticket in self.__tickets:
            totale += ticket.calcolaPreventivo()
        return totale


    def stampaServizi(self):
        print("Servizi Officina", self.nome)
        if len(self.servizi) == 0:
            print("Nessun servizio disponibile")
        else:
            contatore = 0
            for nome, costo in self.servizi.items():
                print(contatore+1, "-", nome, ",", costo)
                contatore += 1


    def calcolaStatisticheTipo(self):
        conteggio = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0}
        for ticket in self.tickets:
            elettro = ticket.get_elettrodomestico()
            if type(elettro) == Lavatrice:
                conteggio["Lavatrice"] += 1
            elif type(elettro) == Frigorifero:
                conteggio["Frigorifero"] += 1
            elif type(elettro) == Forno:
                conteggio["Forno"] += 1
        print("Lavatrici:", conteggio['Lavatrice'])
        print("Frigoriferi:", conteggio['Frigorifero'])
        print("Forni:", conteggio['Forno'])


    def get_tickets(self):
        return self.__tickets
    def get_elettrodomestici(self):
        return self.__elettrodomestici