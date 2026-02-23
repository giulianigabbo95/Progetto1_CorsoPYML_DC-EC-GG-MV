'''
Gruppo Discord: https://discord.gg/VscHwYRe
Tabella di Marcia:  https://docs.google.com/document/d/1-w-js9cxguo0QdjEWh_PbhPzplJr30-gSaY11mGvUc8/edit?usp=sharing
Respository: https://github.com/giulianigabbo95/ProgettoCorso_ECGGMV

Esercizio: Gestionale Officina Elettrodomestici
Progettare un sistema a oggetti per un'officina che ripara elettrodomestici.
Il programma deve modellare elettrodomestici, ticket di riparazione e operazioni dell'officina utilizzando incapsulamento, ereditarietà, polimorfismo, type() e metodi variatici (*args, **kwargs).

1. Classe base: Elettrodomestico:
    Attributi privati (__ (doppio underscore)):
        - __marca (stringa)
        - __modello (stringa)
        - __anno_acquisto (intero)
        - __guasto (stringa)
    Metodi:
        - __init__(self, marca, modello, anno_acquisto, guasto): costruttore
        - descriviElettrodomestico(self): restituisce stringa con marca, modello, anno, guasto
        - stimaCostoBase(self): restituisce un valore numerico (costo base diagnosi)
        - Getter e Setter per tutti gli attributi (controllo: anno non può essere nel futuro)
    Regola 1 - Incapsulamento: attributi privati (__), accessibili solo tramite getter/setter.
    
2. Classi derivate (Ereditarietà + Polimorfismo):
    Creare almeno tre sottoclassi di Elettrodomestico:
    2.1 Lavatrice:
        Attributi aggiuntivi privati:
            - capacita_kg (intero)
            - giri_centrifuga (intero)
        Override:
            - stimaCostoBase(self): costo maggiorato se la capacità è elevata
    2.2 Frigorifero
        Attributi aggiuntivi privati:
            - litri (intero)
            - ha_freezer (booleano)
        Override:
            - stimaCostoBase(self): costo modificato in base a presenza freezer e litri
    2.3 Forno
        Attributi aggiuntivi privati:
            - tipo_alimentazione (stringa: "elettrico", "gas")
            - ha_ventilato (booleano)
        Override:
            - stimaCostoBase(self): costo modificato in base a tipo alimentazione e presenza funzione ventilata
        Regola 2 - Ereditarietà: tutte le classi derivate devono chiamare super().__init__() nel costruttore.
        Regola 3 - Polimorfismo: ogni sottoclasse implementa la propria versione di stimaCostoBase().

3. Classe TicketRiparazione:
    Classe che rappresenta un ticket di riparazione aperto in officina.
    Attributi privati (__):
        - __id_ticket (intero o stringa univoca)
        - __elettrodomestico (oggetto di tipo Elettrodomestico o sottoclasse)
        - __stato (stringa: "aperto", "in lavorazione", "chiuso")
        - __note (lista di stringhe, inizialmente vuota)
    Metodi:
        - __init__(self, id_ticket, elettrodomestico): costruttore
        - aggiungiNota(self, testo): aggiunge una nota alla lista
        - calcolaPreventivo(self, *voci_extra): metodo variadico:
            . Utilizza elettrodomestico.stimaCostoBase() come costo di partenza
            . Somma tutte le voci extra passate come parametri (*voci_extra)
            . Restituisce il totale
        -Getter e setter per stato e note
    Nota: il metodo calcolaPreventivo() deve funzionare con qualsiasi sottoclasse di Elettrodomestico (polimorfismo su stimaCostoBase()).

4. Classe Officina:
    Classe che gestisce i ticket e gli elettrodomestici.
    Attributi:
        - nome (stringa)
        - tickets (lista di oggetti TicketRiparazione)
    Metodi:
        - aggiungiTicket(self, ticket): aggiunge un ticket alla lista
        - chiudiTicket(self, id_ticket): imposta lo stato del ticket su "chiuso"
        - stampaTicketAperti(self): mostra ID, tipo di elettrodomestico e stato
        - totalePreventivo(self): somma i preventivi di tutti i ticket

5. Uso di type() e controllo degli oggetti:
    Implementare un metodo all'interno della classe Officina (o in una funzione separata): calcolaStatisticheTipo(self)
    Questo metodo deve:
        - Iterare su tutti i ticket
        - Utilizzare type() (o isinstance()) per identificare se l'elettrodomestico associato al ticket è una Lavatrice, un Frigorifero o un Forno
        - Contare quanti ticket ci sono per ciascuna sottoclasse
        - Stampare un report del tipo:
            . text
            . Numero di lavatrici in riparazione: X
            . Numero di frigoriferi in riparazione: Y
            . Numero di forni in riparazione: Z
    Requisito: il metodo deve utilizzare type() (o varianti consigliate) per determinare il tipo reale degli oggetti.

'''
from Lavatrice import Lavatrice
from Frigorifero import Frigorifero
from Forno import Forno
from TicketRiparazione import TicketRiparazione
from Officina import Officina

bob_aggiustatutto = Officina("Officina Elettrodomestici Roma")

while True:
    print("")
    print("Menu", bob_aggiustatutto.nome)
    print("Come desideri infastidire i dipendenti sottopagati?")
    print("1. Aggiungi Elettrodomestico")
    print("2. Apri Ticket Riparazione")
    print("3. Aggiungi Servizi Extra a Ticket")
    print("4. Chiudi Ticket")
    print("5. Visualizza Tutti gli Elettrodomestici")
    print("6. Filtra Elettrodomestici per Tipo")
    print("7. Visualizza Totale Incassato")
    print("8. Esci")
    print("")

    scelta = input("Scegli: ")

    match scelta:
        case "1":
            print("Tipo Elettrodomestico da Aggiungere:")
            print("1. Lavatrice")
            print("2. Frigorifero")
            print("3. Forno")
            print("")

            tipo = input("Scegli: ")
            if tipo == '0':
                continue
            marca = input("Marca: ")
            modello = input("Modello: ")
            while True:
                anno = input("Anno Acquisto: ")
                if anno.isdigit() == True and len(anno) == 4:   # Se anno era int avrei usato len(str(anno)) al posto di len(anno)
                    break
                print("Riprova")
            guasto = input("Descrizione Guasto: ")

            match tipo:
                case "1":
                    capacita = int(input("Capacità (Kg): "))
                    giri = int(input("Giri della Centrifuga: "))
                    elettrodom = Lavatrice(marca, modello, anno, guasto, capacita, giri)
                    bob_aggiustatutto.aggiungiElettrodomestico(elettrodom)   
                case "2":
                    litri = int(input("Litri: "))
                    freezer = input("Ha il Freezer? [S]/[N]): ").lower() == "s"
                    elettrodom = Frigorifero(marca, modello, anno, guasto, litri, freezer)
                    bob_aggiustatutto.aggiungiElettrodomestico(elettrodom)
                case "3":
                    while True:
                        alimentazione = input("Tipo di Alimentazione [Elettrico]/[Gas]: ").lower()
                        if alimentazione == "gas" or alimentazione == "elettrico":
                            break
                        else:
                            print("Cosa pensi, che aggiusti utensili a", alimentazione, "o a Carbone? Riprova!")
                    ventilato = input("Ha la Funzione ventilata? [S]/[N]: ").lower() == "s"
                    elettrodom = Forno(marca, modello, anno, guasto, alimentazione, ventilato)
                    bob_aggiustatutto.aggiungiElettrodomestico(elettrodom)
                case _:
                    print("Tipo non valido!")

        case "2":
            if len(bob_aggiustatutto.get_elettrodomestici()) == 0:
                print("Nessun elettrodomestico rimasto in officina!")
                print("Facciamo schifo e non ci chiama nessuno o siamo troppo bravi e veloci a risolvere problemi?")
                continue
            while True:
                id_ticket = input("Inserisci ID per il nuovo ticket: ")
                if not id_ticket.isdigit(): 
                    print("L'ID deve essere un numero!")
                    continue
                for t in bob_aggiustatutto.get_tickets():
                    if t.get_id() == int(id_ticket):
                        print("L'ID", t.get_id(),"è già esistente!")
                        continue
                break
            print("Elettrodomestici disponibili:")
            for i in range(len(bob_aggiustatutto.get_elettrodomestici)):
                print(i+1, "-", bob_aggiustatutto.get_elettrodomestici()[i].descriviElettrodomestico())
            while True:
                selezione = input("Scegli elettrodometico:")
                if selezione.isdigit():
                    idx_elettrodom = int(selezione) - 1
                    if len(bob_aggiustatutto.elettrodomestici) > idx_elettrodom >= 0:
                        ticket = TicketRiparazione(int(id_ticket), bob_aggiustatutto.elettrodomestici[idx_elettrodom])
                        bob_aggiustatutto.tickets.append(ticket)
                        print("Ticket", id_ticket, "aperto!")
                        break
                    else:
                        print("Numero non valido!")
                else:
                    print("Non hai inserito un numero!")

        case "3":
            if len(bob_aggiustatutto.tickets) == 0:
                print("Nessun ticket aperto!")
                continue
            print("Ticket aperti:")
            for t in bob_aggiustatutto.tickets:
                if t.get_stato() == "aperto":
                    print("ID:", t.get_id(), "-", t.get_elettrodomestico().descriviElettrodomestico())
            while True:
                selezione = input("Scelgi ticket aperto: ")
                if selezione.isdigit():
                    id_ticket_scelto = int(selezione)
                    for t in bob_aggiustatutto.tickets:
                        if t.get_id() == id_ticket_scelto and t.get_stato() == "aperto":
                            lista_costo_serv_agg = []
                            print("Servizi extra disponibili:")
                            print("0 - Nessun Servizio, 0 € (Esci)")
                            bob_aggiustatutto.stampaServizi()
                            voci_extra = input("Inserisci Numeri Servizi (interi separati da spazio): ").split()
                            if len(voci_extra) == 1 and voci_extra[0] == 0:
                                print("Ciao")
                                break
                            for strg in voci_extra:
                                if strg.isdigit() == False:
                                    print("Non hai inserito solo numeri interi!")
                                    break
                                idx_serv_agg = int(strg)-1
                                if idx_serv_agg < len(bob_aggiustatutto.servizi_aggiuntivi):
                                    lista_costo_serv_agg.append(bob_aggiustatutto.servizi_aggiuntivi[bob_aggiustatutto.servizi_aggiuntivi()[idx_serv_agg]])
                                else:
                                    print("Seleziona un servizio esistente!")
                                    break
                                print("Il totale del preventivo con servizi extra è:", t.calcolaPreventivo(*lista_costo_serv_agg))
                        else:
                            print("Ticket non trovato o già chiuso!")
                else:
                    print("Devi inserire un ID numerico!")

        case "4":
            if len(bob_aggiustatutto.tickets) == 0:
                print("Nessun ticket aperto!")
                continue
            print("Ticket aperti:")
            for t in bob_aggiustatutto.tickets:
                if t.get_stato() == "aperto":
                    print("ID:", t.get_id(), "-", t.get_elettrodomestico().descriviElettrodomestico())
            while True:
                selezione = input("Scelgi ticket da chiudere: ")
                if selezione.isdigit():
                    id_ticket_scelto = int(selezione)
                    for t in bob_aggiustatutto.tickets:
                        if t.get_id() == id_ticket_scelto:
                            if t.get_stato() == "aperto":
                                t.set_stato("chiuso")
                                print("Ticket", id_ticket_scelto, "chiuso!")
                            else:
                                print("Il ticket", id_ticket_scelto, "è già", ticket.get_stato())
                            break
                    print("Ticket non trovato!")
                else:
                    print("Devi inserire un ID numerico!")

        case "5":
            if len(bob_aggiustatutto.elettrodomestici) == 0:
                print("Nessun elettrodomestico in officina!")
            else:
                print("Elettrodomestici:")
                for i in range(len(bob_aggiustatutto.get_elettrodomestici())):
                    print(i+1, "-", bob_aggiustatutto.get_elettrodomestici()[i].descriviElettrodomestico())

        case "6":
            if len(bob_aggiustatutto.tickets) == 0:
                print("Nessun ticket aperto!")
                continue
            bob_aggiustatutto.calcolaStatisticheTipo()

        case "7":
            if len(bob_aggiustatutto.tickets) == 0:
                print("Nessun ticket aperto!")
                continue
            print("Totale preventivi:", bob_aggiustatutto.calcolaTotalePreventivo(), "€")

        case "8":
            print("Grazie per aver usato il gestionale officina!")
            print("Per farvore non farti più rivedere!")
            break
        
        case _:
            print("Possibile che tu sia così incapace?")