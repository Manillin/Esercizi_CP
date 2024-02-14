import transazione
import users
from colorama import Fore, Style
import datetime
import time
import sys
import pickle


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"
def to_key(x): return x.strip().lower().replace(" ", "")


def crea_backup_utenti(nome_file, struct):
    with open(nome_file, 'wb') as file:
        pickle.dump(struct, file)
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


# MENU

contenitore_utenti = {}
ceo = users.Utente('Fronk', [], 5)
# Format Contenitore Utenti:
# USER_KEY(nospazi) : [ User, [lista_transazioni], saldo ]
#
contenitore_utenti['fronk'] = ceo


while True:
    print(red("\nLista Utenti: "))
    for key, val in contenitore_utenti.values():
        print(green(f"User Key: {key} ; UserName: {val.nominativo}"))

    print(green("\n\n\tMENU: "))
    main_menu_choice = input(green('''

1. Creazione Nuovo Utente
2. Log In Utente
3. Effettuare BackUp o Ripristino 
4. Uscire
                                   '''))
    if main_menu_choice == '1':
        # Logica creazione nuovo utente:
        nominativo = input("Inserisci nominativo: ")
        user_key = to_key(nominativo)
        if user_key in contenitore_utenti:
            print(red("Utente già registrato... Procedi con il Log In"))
            continue
        new_user = users.Utente(nominativo, [], 0)
        contenitore_utenti[user_key] = new_user

    elif main_menu_choice == '2':
        user_key = to_key(input("Chiave o Nominativo User: "))
        if user_key in contenitore_utenti:
            nominativo = contenitore_utenti[user_key]
        else:
            print(red("\nUtente inesistenete..."))
            continue

    elif main_menu_choice == '3':
        pass

    elif main_menu_choice == '4':
        print(red("\nTerminazione..."))
        time.sleep(0.5)
        sys.exit()

    else:
        print(red("Invalid choice...\n"))
        continue

    # Variabile per controllare il sottomenu: User choice
    stay_on_second_menu = False
    while not stay_on_second_menu and nominativo and user_key:
        user = contenitore_utenti[user_key]  # variable classe User
        print(green(f"\n\nBentornato {nominativo} , cosa vuoi fare? "))
        user_choice = input(green(
            f"1. Nuovo Versamento\n2. Nuovo Prelievo\n3. Vedere lo storico delle operazioni\n4. Esportare una OP\n5. Tornare al Menu Principale\n"))

        # possibile scelte:
        if user_choice == '1':
            pass

        elif user_choice == '2':
            pass

        # Vedere lo storico delle operazioni
        elif user_choice == '3':
            scelta_storico = input(green(
                f"\n1. Vedere lo storico intero\n2. Vedere lo storico filtrato per data"))
            if scelta_storico == '1':
                print(green("Lista di tutte le transazioni registrate: "))
                for tran in user.lista_transazioni:
                    print(green(tran), end='\n')

            elif scelta_storico == '2':
                try:
                    data_inizio = ()
                    data_fine = ()
                    lista_transazioni_filtrate = transazione.filtra_data(
                        user.lista_transazioni, data_inizio, data_fine)
                    print(
                        green(f"Transazioni registrate da {data_inizio} <-> {data_fine}"))
                    for transazione_filtrata in lista_transazioni_filtrate:
                        print(green(transazione_filtrata), end='\n')
                except:
                    print(red("Formato data sbagliato! [ YYYY / MM / DD ]"))
                    continue

        elif user_choice == '4':
            pass

        elif user_choice == '5':
            print(green("\nReturning to main menu: "))
            stay_on_second_menu = True

        else:
            print(red("Scelta invalida "))
            continue
