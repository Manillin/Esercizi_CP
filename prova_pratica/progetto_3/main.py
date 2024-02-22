import sys
from colorama import Fore, Style
import pickle
import paziente
import farmaco
import time


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"
def to_key(x): return x.strip().lower().replace(" ", "")


contenitore_pazienti = {}
# menu:
while True:
    print(red("Lista Pazienti: "))
    for key, val in contenitore_pazienti.items():
        print(green(f"Key: {key} - Nominativo: {val.nominativo}"))
    print(green("\n\n\tMENU: "))
    main_menu_choice = input(green('''

1. Creare nuovo paziente
2. Log in Paziente
3. Effettuare BackUp o Ripristino 
4. Uscire\n
'''))

    # Scelte:
    if main_menu_choice == '1':
        nominativo = input("\nInserisci nome e cognome nuovo paziente\n")
        if nominativo:
            paziente_attuale = paziente.Paziente(nominativo, [])
            contenitore_pazienti[to_key(nominativo)] = paziente_attuale
        else:
            print(red("Non puoi creare un pazinete senza nominativo\n"))
            continue

    elif main_menu_choice == '2':
        login_nominativo = input("Inserisci nominativo per log in: ")
        login_key = to_key(login_nominativo)
        if login_key in contenitore_pazienti:
            paziente_attuale = contenitore_pazienti[login_key]
        else:
            print(red("\Paziente inesistente...\n"))
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
            # ->users.crea_backup_utenti(nome_file, contenitore_utenti)
            continue
        elif backup_choice == '2':  # ripristinare da backup
            # ->contenitore_utenti = users.load_backup_utenti(nome_file)
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
    # and controllo istanza classe utente
    while not stay_on_second_menu and (to_key(nominativo) in contenitore_pazienti):
        paziente_attuale:'paziente.Paziente' = contenitore_pazienti[to_key(nominativo)]
        print(green(f"\nPaziente selezionato: {paziente_attuale.nominativo} \n"))
        # Sub Menu
        user_choice = input(
            green(f"1. Inserire uno o più farmaci per il paziente\n2. Visualizzare la terapia attuale
                  \n3. Visualizzare la terapia dei giorni successivi\n4. Tornare al Menu Principale")
        )
        if user_choice == '1':
            farmaci = "."
            while farmaci:
                print(green(f"Inserisci i farmaci che desideri: [Premi enter quando hai finito]\n"))
                farmaci = input(": ")
                frequenza = int(input("Con qale frequenza: "))
                if farmaci and frequenza:
                    new_farmaco = farmaco.Farmaco(farmaci, frequenza)
                    paziente_attuale.lista_farmaci.append(new_farmaco)
                else:
                    print(red("Input sbagliato!"))
                    continue

        elif user_choice == '2':
            if paziente_attuale.lista_farmaci:
                print(green(f"Terapia odieran di: {paziente_attuale.nominativo}"))
                counter = 0
                for farmaco_paziente in paziente_attuale.lista_farmaci:
                    print(green(f"{counter}. {farmaco_paziente}"), end='\n')
            

        elif user_choice == '3':
            pass

        elif user_choice == 'X':
            print(green("Returning to Main Menu ... "))
            time.sleep(0.3)
            stay_on_second_menu = True
        else:
            print(red("Scelta Invalida!\n"))
