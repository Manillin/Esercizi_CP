import farmaco
from colorama import Fore, Style
import pickle


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


class Paziente:
    def __init__(self, nominativo, lista_farmaci=None) -> None:
        self.nominativo = nominativo
        self.lista_farmaci: list['farmaco.Farmaco'] = lista_farmaci if lista_farmaci is not None else [
        ]


def print_terapia_giorni_successivi(paziente: 'Paziente', giorni):
    print()
    for g in range(giorni):
        print(green(f"Giorno: {g+1}"))
        for farmac in paziente.lista_farmaci:
            if (g+1) % farmac.frequenza == 0:
                print(green(farmac.nominativo))
        print()


def crea_backup_pazienti(nome_file, contenitore_utenti):
    with open(nome_file, 'wb') as file:
        pickle.dump(contenitore_utenti, file)
    print(green(f"\nBack up pazienti salvato con successo in: {nome_file} "))


def load_backup_pazienti(nome_file):
    try:
        with open(nome_file, 'rb') as file:
            utenti = pickle.load(file)
        print(green(f"\nPazienti ripristinati con successo da: {nome_file}"))
        return utenti
    except:
        print(red(f"\nRipristino pazienti fallito..."))
        return []


def check_farmaco_by_name(nome_farmaco, paziente: Paziente):
    for farmaco in paziente.lista_farmaci:
        if nome_farmaco == farmaco.nominativo:
            return farmaco
    return None
