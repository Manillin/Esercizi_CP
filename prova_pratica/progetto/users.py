class Utente:
    def __init__(self, nominativo, stipendio, orario) -> None:
        self.nominativo = nominativo
        self.stipendio = stipendio
        self.orario = orario


class Subordinato(Utente):
    def __init__(self, nominativo, stipendio, orario) -> None:
        super().__init__(nominativo, stipendio, orario)
        self.storico_richieste_pagamento = []

    def nuova_richiesta_pagamento(self):
        pass


class Responsabile(Utente):
    def __init__(self, nominativo, stipendio, orario) -> None:
        super().__init__(nominativo, stipendio, orario)
        self.lista_subordinati = []
