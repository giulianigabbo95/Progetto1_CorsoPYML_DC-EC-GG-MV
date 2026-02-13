"""Classe Ticket Riparazione:
Classe che rappresenta un ticket di riparazione aperto in officina.
Attributi privati (__):
__id_ticket (intero o stringa univoca)
__elettrodomestico (oggetto di tipo Elettrodomestico o sottoclasse)
__stato (stringa: "aperto", "in lavorazione", "chiuso")
__note (lista di stringhe, inizialmente vuota)
Metodi:
__init__(self, id_ticket, elettrodomestico): costruttore
aggiungiNota(self, testo): aggiunge una nota alla lista
calcolaPreventivo(self, *voci_extra): metodo variadico:
Utilizza elettrodomestico.stimaCostoBase() come costo di partenza
Somma tutte le voci extra passate come parametri (*voci_extra)
Restituisce il totale
Getter e setter per stato e note
Nota: il metodo calcolaPreventivo() deve funzionare con qualsiasi sottoclasse di Elettrodomestico (polimorfismo su stimaCostoBase())."""

class TicketRiparazione:
    def __init__(self, id_ticket, elettrodomestico):
        # Attributi privati come richiesto (Regola 1: Incapsulamento)
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico # Oggetto (Lavatrice, Frigo o Forno)
        self.__stato = "aperto"                    # Stato iniziale di default
        self.__note = []                           # Lista vuota per i log della riparazione

    # --- METODI RICHIESTI ---

    def aggiungiNota(self, testo):
        """Aggiunge una stringa alla lista delle note del ticket."""
        self.__note.append(testo)

    def calcolaPreventivo(self, *voci_extra):
        """
        METODO VARIADICO: accetta un numero variabile di costi (float o int).
        Sfrutta il POLIMORFISMO: chiama stima_costo_base() senza sapere 
        se l'oggetto è un Forno, una Lavatrice o un Frigo.
        """
        # 1. Recupera il costo base specifico dell'elettrodomestico (Polimorfismo)
        totale = self.__elettrodomestico.stima_costo_base()
        
        # 2. Somma tutti i parametri extra passati tramite *voci_extra
        # voci_extra viene trattato come una tupla all'interno del metodo
        for costo in voci_extra:
            totale += costo
            
        return totale

    """Getter e setter impostati tramite @property per blindare le variabili e impedire manipolazioni errate"""

    @property
    def stato(self):
        return self.__stato

    @stato.setter
    def stato(self, nuovo_stato):
        stati_validi = ["aperto", "in lavorazione", "chiuso"]
        if nuovo_stato.lower() in stati_validi:
            self.__stato = nuovo_stato.lower()
        else:
            print(f"Errore: Stato '{nuovo_stato}' non valido.")

    @property
    def note(self):
        # Restituiamo una copia o la lista formattata per proteggere l'originale
        return "\n".join(self.__note) if self.__note else "Nessuna nota presente."

    # Getter per l'elettrodomestico (utile per il metodo statisticheTipo dell'Officina)
    def get_elettrodomestico(self):
        return self.__elettrodomestico
    
    def get_id(self):
        return self.__id_ticket
    
    """# Crei il forno (fatto da te)
mio_forno = Forno("Samsung", "Dual Cook", 2023, "Ventola rumorosa", "elettrico", True)

# Crei il ticket (fatto da te)
t1 = TicketRiparazione("TK-001", mio_forno)

# Aggiungi note e calcoli il preventivo con extra
t1.aggiungiNota("Sostituito cuscinetto ventola")
preventivo_finale = t1.calcolaPreventivo(25.0, 15.5) # Extra: pezzo + spedizione

print(f"Totale per ticket {t1.get_id()}: {preventivo_finale}€")"""