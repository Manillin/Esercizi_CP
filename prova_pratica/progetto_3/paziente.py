

class Paziente:
    def __init__(self, nominativo, lista_farmaci=None) -> None:
        self.nominativo = nominativo
        self.lista_farmaci = lista_farmaci if lista_farmaci is not None else []
