'''
Esercizio: Gestionale Officina Elettrodomestici
Progettare un sistema a oggetti per un'officina che ripara elettrodomestici.
Il programma deve modellare elettrodomestici, ticket di riparazione e operazioni dell'officina utilizzando incapsulamento, ereditarietà, polimorfismo, type() e metodi variatici (*args, **kwargs).

1. Classe base: Elettrodomestico:
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

3. Classe Ticket Riparazione:
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
    Implementare un metodo all'interno della classe Officina (o in una funzione separata): statisticheTipo(self)
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




'''
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
    

# Metodo altenativo 1 alla riga superiore:
    scelta_ventilato = input("Ha funzione ventilata? (s/n): ").lower()
    
    if scelta_ventilato == "s"
        ventilato = True
    elif scelta_ventilato == "n"
        ventilato == False
    else
        print("Inserimento non corretto. Imposto NON ventilato di default")
        ventilato = False

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


    forno_1 = Forno(marca, modello, anno, guasto, alimentazione, ventilato)
    officina.aggiungi_elettrodomestico(elettro)
    
'''