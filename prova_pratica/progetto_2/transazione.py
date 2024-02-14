from colorama import Fore, Style
import datetime
import time
import sys
import pickle


class Transazione:
    def __init__(self, data, ammontare, tipo) -> None:
        self.data = data
        self.ammontare = ammontare
        self.tipo = tipo


def filtra_data(transazioni: list['Transazione'], data_inizio, data_fine):
    res = []
    for tran in transazioni:
        if (tran.data >= data_inizio and
                tran.data <= data_fine
                ):
            res.append(tran)
    return res


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def verde(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


if __name__ == '__main__':
    pass
