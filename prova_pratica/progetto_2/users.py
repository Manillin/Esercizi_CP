import pickle
from colorama import Fore, Style


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


class Utente:
    def __init__(self, nominativo, lista_transazioni=None, saldo=0) -> None:
        self.nominativo = nominativo
        self.lista_transazioni = lista_transazioni if lista_transazioni is not None else []
        self.saldo = saldo


def crea_backup_utenti(nome_file, struct):
    with open(nome_file, 'wb') as file:
        pickle.dump(struct, file)
        print("Y")
    print(green(f"Back Up utenti salvato con successo in: {nome_file} "))


def load_backup_utenti(nome_file):
    try:
        with open(nome_file, 'rb') as file:
            utenti = pickle.load(file)
        print(green(f"Utenti ripristinati con successo!\n"))
        return utenti
    except:
        print(red("Ripristino Fallito!\n"))
        return []
