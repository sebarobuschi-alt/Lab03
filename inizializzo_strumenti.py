
class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.__id_strumento = id_strumento
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = int(anno_acquisto)
        self.__valore = float(valore)

    @property
    def id_strumento(self):
        return self.__id_strumento
    @property
    def tipo(self):
        return self.__tipo
    @property
    def marca(self):
        return self.__marca
    @property
    def anno_acquisto(self):
        return self.__anno_acquisto
    @property
    def valore(self):
        return self.__valore


    @id_strumento.setter
    def id_strumento(self,id_strumento):
        self.__id_strumento = id_strumento

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @marca.setter
    def marca(self,marca):
        self.__marca = marca

    @anno_acquisto.setter
    def anno_acquisto(self,anno_acquisto):
        self.__anno_acquisto = anno_acquisto
    @valore.setter
    def valore(self,valore):
        self.__valore = valore

    def __str__(self):
        """Restituisce una stringa formattata quando si stampa l'oggetto Strumento"""
        return f"[{self.__id_strumento}] - {self.__tipo} - Marca: {self.__marca} - Anno: {self.__anno_acquisto} - Valore: {self.__valore:.2f} €"
