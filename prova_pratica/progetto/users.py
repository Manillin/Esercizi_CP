class Utente:
    def __init__(self, nominativo, stipendio, orario) -> None:
        self.nominativo = nominativo
        self.stipendio = stipendio
        self.orario = orario


class Subordinato(Utente):
    def __init__(self, nominativo, stipendio, orario, responsabile) -> None:
        super().__init__(nominativo, stipendio, orario)
        self.responsabile = responsabile
        self.richieste_pag = []

    def get_richieste(self):
        return self.richieste_pag

    def get_index(self, id):
        for index in range(len(self.richieste_pag)):
            req = self.richieste_pag[index]
            if req[0] == id:
                return index
        return "Error"


class Responsabile(Utente):
    def __init__(self, nominativo, stipendio, orario) -> None:
        super().__init__(nominativo, stipendio, orario)
        self.lista_subordinati = []
