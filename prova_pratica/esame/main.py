import datetime
import sys
import time
from colorama import Fore, Style
import sys
import pickle

import utente
import appuntamento


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"
def to_key(x): return x.strip().lower().replace(" ", "")


if __name__ == '__main__':
    # Inizio Main e Menu:
    # HashMap per contenere utenti e classi
    contenitore_utenti = {}
    utente0 = utente.Utente("Utente 1", [])
    contenitore_utenti[to_key(utente0.nominativo)] = utente0

    # menu:
    while True:
        print(red("Lista utenti: "))
        for key, val in contenitore_utenti.items():
            print(green(f"Key: {key} - Nominativo: {val.nominativo} "))
        print(green("\n\n\tMENU: "))
        main_menu_choice = input(green('''

1. Creare nuovo Utente
2. Log in Utente
3. Effettuare BackUp o Ripristino                             
4. Uscire\n
'''))

        # Scelte:
        if main_menu_choice == '1':
            # creazione utente
            nominativo = input("Inserisci nominativo utente: ")
            user_key = to_key(nominativo)
            if user_key in contenitore_utenti:
                print(red("Utente già registrato... Procedi con il Log In"))
                continue
            user = utente.Utente(nominativo, [], [])
            contenitore_utenti[user_key] = user

        elif main_menu_choice == '2':
            user_key = to_key(input("Chiave o nominativo utente: "))
            if user_key in contenitore_utenti:
                user = contenitore_utenti[user_key]
            else:
                print(red("\nUtente inesistenete..."))
                continue

        # esempio di choice con submenu
        elif main_menu_choice == '3':
            menu_ripristino = '''\n
1. Effettuare un BackUp degli utenti attuali 
2. Ripristinare stato da un precedente backup
3. Tornare al menu principale\n
    '''
            print(green(menu_ripristino))
            nome_file = 'backup.pkl'
            backup_choice = input(": ")
            if backup_choice == '1':  # fare backup
                utente.crea_backup_utenti(nome_file, contenitore_utenti)
                continue
            elif backup_choice == '2':  # ripristinare da backup
                contenitore_utenti = utente.load_backup_utenti(nome_file)
                continue
            elif backup_choice == '3':
                continue
            else:
                print(red("\nInvalid choice, torno al menu principale"))
                continue

        elif main_menu_choice == '4':
            print(red("\nTerminazione..."))
            time.sleep(0.5)
            sys.exit()

        else:
            print(red("Invalid choice!\n"))
            # continue

        # var per controllare il sottomenu: User choice
        stay_on_second_menu = False
        while not stay_on_second_menu and user:  # and controllo istanza classe utente
            print(
                green(f"\nBentornato {user.nominativo}, cosa vuoi fare?: \n"))
            user_choice = input(
                green(f"1. Inserire nuovi appuntamenti \n2. Eliminare appuntamento\n3. Visualizzare appuntamenti di un giorno\n4. Visualizzare appuntamenti in un range di data \n5. Tornare al Menu Principale\n:")
            )
            if user_choice == '1':
                nome_appuntamento = '.'
                while nome_appuntamento:
                    nome_appuntamento = input(
                        "Nome appuntamento: [Premi ENTER per uscire]\n")
                    if nome_appuntamento:
                        data = input(
                            "Inserisci data appuntamento: [YYYY/MM/DD]\n")
                        try:
                            data = appuntamento.string_to_data(data)
                        except:
                            print(red("Formato data errato!"))

                        nuovo_appuntamento = appuntamento.Appuntamento(
                            nome_appuntamento, data)
                        user.calendario.append(nuovo_appuntamento)

                        # Chiedi all'utente se vuole specificare un altro utente
                        inserire_altro_utente = input(
                            "Vuoi inserire tale appuntamento nel calendario di un altro utente? (s) o (n): ").lower()

                        while inserire_altro_utente == 's':
                            second_user_key = to_key(
                                input("Nominativo dell'altro utente: "))
                            if second_user_key in contenitore_utenti:
                                appuntamento.inserisci_appuntamento_user(
                                    second_user_key, contenitore_utenti, nuovo_appuntamento)

                                # Aggiunta alla lista appuntamenti condivisi
                                user.appuntamenti_condivisi.append(
                                    contenitore_utenti[second_user_key])
                                contenitore_utenti[second_user_key].appuntamenti_condivisi.append(
                                    user)

                                print(green(
                                    f"Appuntamento inserito anche per {contenitore_utenti[second_user_key].nominativo}"))
                            else:
                                print(
                                    red("Utente Inesistente, interruzione processo!\n"))
                                break

                            # Chiedi all'utente se vuole specificare un altro utente
                            inserire_altro_utente = input(
                                "Vuoi inserire tale appuntamento nel calendario di un altro utente? (s) o (n): ").lower()

                    else:
                        print(red("Torno al menu!\n"))
                        break

            elif user_choice == '2':
                for app in user.calendario:
                    print(app.print_appuntamento())

                appuntamento_target = int(
                    input("Inserisci l'ID dell'appuntamento che vuoi cancellare: \n"))
                print(appuntamento.delete_appuntamento_by_ID(user,
                                                             user.calendario, appuntamento_target))
            elif user_choice == '3':
                data_singola = input("Inserisci la data: \n")
                data_singola = appuntamento.string_to_data(data_singola)
                lista_appuntamenti = utente.filtra_data_giorno(
                    user.calendario, data_singola)
                if lista_appuntamenti:
                    print(
                        green(f"Appuntamenti del: {lista_appuntamenti[0].data}"))
                    for app in lista_appuntamenti:
                        print(green(app.nome))
                else:
                    print(red("Non sono presenti appuntamenti per quella data!\n"))
                    continue

            elif user_choice == '4':
                data_inizio = input("Inserisci data inizio: \n")
                data_fine = input("Inserisci data fine: \n")
                data_inizio = appuntamento.string_to_data(data_inizio)
                data_fine = appuntamento.string_to_data(data_fine)
                lista_appuntamenti = utente.filtra_data_range(
                    user.calendario, data_inizio, data_fine)
                if lista_appuntamenti:
                    appuntamento.stampa_appuntamenti_per_giorno(
                        lista_appuntamenti)
                else:
                    print(red("Nessun appuntamento\n"))

            elif user_choice == '5':
                print(green("Returning to Main Menu ... "))
                time.sleep(0.3)
                stay_on_second_menu = True
            else:
                print(red("Scelta Invalida!\n"))
