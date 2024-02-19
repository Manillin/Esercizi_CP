import datetime
from colorama import Fore, Style


# def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"
# def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"


class Transazione:
    def __init__(self, data, ammontare, tipo) -> None:
        self.data = data
        self.ammontare = ammontare
        self.tipo = tipo

    def print_transazione(self):
        return f"[{self.data} - {self.ammontare}€ - {self.tipo}]"


def filtra_data(transazioni: list['Transazione'], data_inizio, data_fine) -> list['Transazione']:
    res = []
    for tran in transazioni:
        if (tran.data >= data_inizio and
                tran.data <= data_fine
                ):
            res.append(tran)
    return res


def filtra_data_Debug(transazioni: list['Transazione'], data_inizio, data_fine):
    res = []
    print(f"{data_inizio}  -  {data_fine}\n")
    for tran in transazioni:
        print(green(f"{tran.data}"))
        if (tran.data >= data_inizio and
                tran.data <= data_fine
                ):
            res.append(tran)
            print(green("appended"))
    return res


if __name__ == '__main__':

    # Esempio d'uso come script:
    #     python3 -m transazione -h -> in line Helper
    #     python3 -m transazione backup.pkl 2000/10/10 2025/10/10 transazioni.txt
    import users
    import argparse
    import main

    def string_to_data(string: str):
        string = string.replace(" ", "")
        componenti_data = string.split("/")
        anno = int(componenti_data[0])
        mese = int(componenti_data[1])
        giorno = int(componenti_data[2])
        data = datetime.date(anno, mese, giorno)
        return data

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help='Nome del file di backup')
    parser.add_argument(
        'data_inizio', help='Data Inizio in formato [YYYY/MM/DD]')
    parser.add_argument('data_fine', help='Data Fine in formato [YYYY/MM/DD]')
    parser.add_argument('file_destinazione',
                        help='Nome del file su cui esportare')

    args = parser.parse_args()
    file_backup = args.file_name
    data_inizio = string_to_data(args.data_inizio)
    data_fine = string_to_data(args.data_fine)
    dest_file = args.file_destinazione

    contenitore_utenti = users.load_backup_utenti(file_backup)
    print(
        main.green(f"\nDati:\nNome file: {file_backup}\n"))
    res = []
    for utente in contenitore_utenti.values():
        transazioni_filtered = filtra_data(
            utente.lista_transazioni, data_inizio, data_fine)
        for transazione_singola in transazioni_filtered:
            res.append(transazione_singola)

    counter = 1
    with open(dest_file, 'w') as file:
        for tran in res:
            file.write(f"{counter}.  {tran.print_transazione()}\n")
            counter += 1
    print(
        main.green(f"\nTransazioni esportate con successo in {dest_file}! \n")
    )
