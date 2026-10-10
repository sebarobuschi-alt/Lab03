class Prestito:
    def __init__(self,id_prestito,data,id_strumento,cognome_allievo):
        self.__id_prestito = id_prestito
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo

    @property
    def id_prestito(self):
        return self.__id_prestito
    @property
    def data(self):
        return self.__data
    @property
    def id_strumento(self):
        return self.__id_strumento
    @property
    def cognome_allievo(self):
        return self.__cognome_allievo
    def __str__(self):
        return f"[{self.__id_prestito}]- Data: {self.__data} - Strumento: {self.__id_strumento} - Allievo: {self.__cognome_allievo}"