import users
from colorama import Fore, Style
import argparse


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def verde(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"
def to_key(x): return x.strip().lower().replace(" ", "")


def new_richiesta_pagamento(selected_user):
    if isinstance(selected_user, users.Subordinato):
        stato_richiesta = 'pending'
        id_richiesta = len(selected_user.richieste_pag)
        ore_richiesta = int(input("Ore totali della richiesta: "))
        selected_user.richieste_pag.append(
            [id_richiesta, ore_richiesta, stato_richiesta])
    else:
        print(red("Richiesta di pagamento non disponsibile per 'Responsabile'\n"))
        return None


def cronologia_richieste(selected_user):
    if isinstance(selected_user, users.Subordinato):
        if selected_user.richieste_pag:
            print(verde("Richieste pagamento precedenti: "))
            for richiesta in selected_user.richieste_pag:
                print(richiesta)
        else:
            print("Nessuna richiesta trovata...\n")
    else:
        print(red("Cronologia richieste non disponsibile per 'Responsabile'\n"))
        return None


def ore_importo_complessivi(selected_user):
    lista_importi = []
    ore_totali = 0

    for richiesta in selected_user.richieste_pag:
        if richiesta[2] == 'approved':
            lista_importi.append(richiesta)
            ore_totali += richiesta[1]
    return lista_importi, ore_totali


def ore_importo_complessivi2(selected_user):
    ore_totali = 0
    for richiesta in selected_user.richieste_pag:
        if richiesta[2] == 'approved':
            ore_totali += richiesta[1]
    return ore_totali


def richieste_subordinati(selected_user, contenitore_utenti):
    if isinstance(selected_user, users.Responsabile):
        lista_richieste = []
        print(red("\nLista Subordinati: \n"))
        for sub in selected_user.lista_subordinati:
            print(verde(sub.nominativo))
        for subordinato in selected_user.lista_subordinati:
            for r in range(len(contenitore_utenti[to_key(subordinato.nominativo)].get_richieste())):
                lista_richieste.append(
                    [contenitore_utenti[to_key(subordinato.nominativo)].richieste_pag[r], subordinato.nominativo])

        for richiesta in lista_richieste:
            print(richiesta)
    else:
        print(red("\nNon hai subordinati con richieste valide...\n"))
        return None


def modifica_richiesta(selected_user, index, choice, contenitore_utenti, sub_key):
    if isinstance(selected_user, users.Responsabile):
        target = contenitore_utenti[sub_key].richieste_pag[index]
        if choice == 'a':
            target[2] = 'approved'
        else:
            target[2] = 'rejected'
        print(verde(
            f"Debug: <<Richieste per utente {contenitore_utenti[sub_key].nominativo} >>"))
        print(contenitore_utenti[sub_key].get_richieste())
    else:
        print(red("Missing auth to modify requests"))


def load_backup_utenti(nome_file):
    try:
        with open(nome_file, 'rb') as file:
            utenti = pickle.load(file)
        print(verde(f"\nUtenti ripristinati con successo da: {nome_file}"))
        return utenti
    except:
        print(red(f"\nRipristino utenti fallito..."))
        return []


# Istruzioni in caso lanciato come script ( -m + argv)
# Deve passare:
#       - File destinato per l'esportazione
#       - Utente cui esportare richieste
if __name__ == "__main__":
    import pickle
    import main
    import sys

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help='Nome del file di backup')
    parser.add_argument('user', help='Nominativo (senza spazi)')
    parser.add_argument('file_destinazione',
                        help='Nome del file su cui esportare')
    args = parser.parse_args()
    file_name = args.file_name
    user_key = args.user
    dest_file = args.file_destinazione

    contenitore_utenti = main.load_backup_utenti(file_name)
    if user_key not in contenitore_utenti:
        print(red("Utente NON trovato, usa una key valida (nominativo senza spazi)\n"))
        sys.exit()
    print(
        verde(f"\nDati:\nNome file: {file_name}\nNominativo user: {contenitore_utenti[user_key].nominativo}"))

    user = contenitore_utenti[user_key]
    if isinstance(user, users.Responsabile):
        print(red("Hai inserito un responsabile, non esistono richieste di pagamento per questo utente\nInserisci nominativo di un subordinato!\n"))
        sys.exit()
    with open(dest_file, 'w') as file:
        file.write(f"User: {contenitore_utenti[user_key].nominativo}\n\n")
        for richiesta in user.richieste_pag:
            req = str(richiesta)
            file.write(req)
            file.write("\n")
    print(verde("\nEsportazione conclusa con successo!\n"))

    # Esempio uso script:
    #    python3 -m richieste -> per il helper
    #    python3 -m richieste
    #
    #
