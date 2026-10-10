from sys import set_coroutine_origin_tracking_depth
from operator import attrgetter
from inizializzo_prestiti import Prestito
from inizializzo_strumenti import Strumento
from csv import reader

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile
        self.__strumenti = []
        self.__prestiti = []
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self,responsabile):
        self.__responsabile = responsabile

    def aggiorna_responsabile(self,nuovo_responsabile):
        self.__responsabile = nuovo_responsabile
        return self
    def __str__(self):
        return f"Deposito: {self.__nome} - Responsabile: {self.__responsabile}"



    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with (open(file_path, "r")) as in_file:
                csv_reader = reader(in_file)
                for line in csv_reader:
                    if not line:
                        continue
                    s = Strumento(
                        line[0].strip(),
                        line[1].strip(),
                        line[2].strip(),
                        int(line[3].strip()),
                        float(line[4].strip())
                    )
                    self.__strumenti.append(s)

        except FileNotFoundError:
            print("File non trovato")




    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if len(self.__strumenti) == 0:
            id_strumento = 'S1'
        else:
            ultimo_id_s = len(self.__strumenti) + 1
            id_strumento = 'S' + str(ultimo_id_s + 1)
        nuovo_strumento = Strumento(id_strumento,tipo,marca,anno_acquisto,valore)
        self.__strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.__strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        strumento_esiste = False
        for s in self.__strumenti:
            if s.id_strumento == id_strumento:
                strumento_esiste = True
                break

        if not strumento_esiste:
                raise Exception('Strumento inesistente nel deposito')


        for p in self.__prestiti:
                if p.id_strumento == id_strumento:
                    raise Exception('Strumento già in prestito')


        if len(self.__prestiti) == 0:
            id_prestito = 'P1'

        else:
            id_prestito = 'P' + str(len(self.__prestiti) + 1)

        nuovo_prestito = Prestito(id_prestito,data,id_strumento,cognome_allievo)
        self.__prestiti.append(nuovo_prestito)
        return nuovo_prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestito_trovato = False
        for p in self.__prestiti:
            if id_prestito == p.id_prestito:
                self.__prestiti.remove(p)
                prestito_trovato = True

                break

        if not prestito_trovato:
            raise Exception('Il codice del prestito inserito non esiste!')
