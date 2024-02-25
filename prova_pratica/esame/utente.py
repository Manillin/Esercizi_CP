import appuntamento
import datetime
import pickle
from colorama import Fore, Style
import time
import sys


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


class Utente:
    def __init__(self, nominativo, calendario=[], appuntamenti_condivisi=[]) -> None:
        self.nominativo = nominativo
        self.calendario: list['appuntamento.Appuntamento'] = calendario if calendario is not None else [
        ]
        self.appuntamenti_condivisi: list['Utente'] = appuntamenti_condivisi if appuntamenti_condivisi is not None else [
        ]


def filtra_data_giorno(calendario: list['appuntamento.Appuntamento'], data_visualizzazione):
    res = []
    for appuntamento in calendario:
        if appuntamento.data == data_visualizzazione:
            res.append(appuntamento)
    return res


def filtra_data_range(calendario: list['appuntamento.Appuntamento'], data_inizio, data_fine):
    res = []
    for appuntamento in calendario:
        if (appuntamento.data >= data_inizio and
                appuntamento.data <= data_fine):
            res.append(appuntamento)
    return res


def crea_backup_utenti(nome_file, struct):
    with open(nome_file, 'wb') as file:
        pickle.dump(struct, file)
    print(green(f"Back-up utenti salvato con successo in: {nome_file}!\n"))


def load_backup_utenti(nome_file):
    try:
        with open(nome_file, 'rb') as file:
            utenti = pickle.load(file)
        print(green(f"Utenti ripristinati con successo!\n"))
        return utenti
    except:
        print(red("Ripristino Fallito! Terminazione programma "))
        time.sleep(0.5)
        sys.exit()
