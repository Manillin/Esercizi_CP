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
paziente_zero = paziente.Paziente("Paziente 1", [])
contenitore_pazienti[to_key("Paziente 1")] = paziente_zero
# menu:
while True:
    print(red("\n\nLista Pazienti: "))
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
        nominativo = input("Inserisci nominativo per log in: ")
        login_key = to_key(nominativo)
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
            paziente.crea_backup_pazienti(nome_file, contenitore_pazienti)
            continue
        elif backup_choice == '2':  # ripristinare da backup
            contenitore_pazienti = paziente.load_backup_pazienti(nome_file)
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
    while not stay_on_second_menu:
        paziente_attuale: 'paziente.Paziente' = contenitore_pazienti[to_key(
            nominativo)]
        print(
            green(f"\nPaziente selezionato: {paziente_attuale.nominativo} \n"))
        # Sub Menu
        user_choice = input(
            green(f"1. Inserire uno o più farmaci per il paziente\n2. Visualizzare la terapia odierna\n3. Visualizzare la terapia dei giorni successivi\n4. Eliminare un farmaco \n5. Esportare terapia\n6. Tornare al Menu Principale\n"))
        if user_choice == '1':
            farmaci = "."
            while farmaci:
                print(
                    green(f"Inserisci i farmaci che desideri: [Premi enter quando hai finito]\n"))
                farmaci = input("Nome farmaco: ")
                if farmaci:
                    frequenza = int(input("Con quale frequenza: "))
                    new_farmaco = farmaco.Farmaco(farmaci, frequenza)
                    paziente_attuale.lista_farmaci.append(new_farmaco)
                else:
                    print(red("\nTorno al menu!\n"))
                    continue

        elif user_choice == '2':
            if paziente_attuale.lista_farmaci:
                print(
                    green(f"Terapia odieran di: {paziente_attuale.nominativo}\n"))
                counter = 0
                for farmaco_paziente in paziente_attuale.lista_farmaci:
                    print(
                        green(f"{counter}. {farmaco_paziente.nominativo}"), end='\n')
                    counter += 1
            else:
                print(red("Il paziente selezionato non ha ancora una terapia!"))
                continue

        elif user_choice == '3':
            giorni = int(input("Numero di giorni: "))
            paziente.print_terapia_giorni_successivi(paziente_attuale, giorni)

        elif user_choice == '4':
            nome_farmaco = input(
                green("Quale farmaco vuoi cancellare?: "))
            farmaco_da_cancellare = paziente.check_farmaco_by_name(
                nome_farmaco, paziente_attuale)
            if farmaco_da_cancellare and farmaco_da_cancellare in paziente_attuale.lista_farmaci:
                paziente_attuale.lista_farmaci.remove(farmaco_da_cancellare)
                print(red(f"Farmaco rimosso! \n"))
            else:
                print(red("Farmaco non presente nella lista!\n"))
        elif user_choice == '5':
            nome_file = "terapia.txt"
            n_giorni = input("Numero giorni: ")
            with open(nome_file, 'w') as f:
                print(
                    green(f"Terapia odieran di: {paziente_attuale.nominativo}\n"))
                counter = 0
                for farmaco_paziente in paziente_attuale.lista_farmaci:
                    print(
                        green(f"{counter}. {farmaco_paziente.nominativo}"), end='\n')
                    counter += 1
                paziente.print_terapia_giorni_successivi(
                    paziente_attuale, n_giorni)

        elif user_choice == '6':
            print(green("Returning to Main Menu ... "))
            time.sleep(0.3)
            stay_on_second_menu = True
        else:
            print(red("Scelta Invalida!\n"))
