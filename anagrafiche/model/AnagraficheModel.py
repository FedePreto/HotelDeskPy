import sqlite3
from cliente.model.ClienteModel import ClienteModel
from dipendente.model.DipendenteModel import DipendenteModel
from fornitore.model.FornitoreModel import FornitoreModel


class AnagraficheModel():
    def __init__(self):
        self.listaclienti = []
        self.listafornitori = []
        self.listadipendeti = []
        self.get_listaclienti()
        self.get_listafornitori()
        self.get_listadipendenti()

    def get_listaclienti(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_clienti = cursor.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.listaclienti.append(ClienteModel(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4],
                                                  cliente[5], cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20], cliente[21]))
    def get_listafornitori(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_fornitori = cursor.execute('SELECT * FROM Fornitori;').fetchall()
        for fornitore in tab_fornitori:
            self.listafornitori.append(FornitoreModel(fornitore[0], fornitore[1], fornitore[2], fornitore[3], fornitore[4],
                                                      fornitore[5], fornitore[6], fornitore[7], fornitore[8], fornitore[9],
                                                      fornitore[10], fornitore[11]))

    def get_listadipendenti(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_dipendenti = cursor.execute('SELECT * FROM Dipendenti;').fetchall()
        for dipendente in tab_dipendenti:
            self.listadipendeti.append(DipendenteModel(dipendente[0], dipendente[1], dipendente[2], dipendente[3], dipendente[4],
                                                       dipendente[5], dipendente[6], dipendente[7], dipendente[8], dipendente[9]))
