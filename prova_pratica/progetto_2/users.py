class Utente:
    def __init__(self, nominativo, lista_transazioni=None, saldo=0) -> None:
        self.nominativo = nominativo
        self.lista_transazioni = lista_transazioni if lista_transazioni is not None else []
        self.saldo = saldo
