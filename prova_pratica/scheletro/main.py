# import #classe
import sys
import time
from colorama import Fore, Style
import sys
import pickle


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


# Da mettere nel file User o simile:

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


# Inizio Main e Menu:

# HashMap per contenere utenti e classi
contenitore_utenti = {}
# Creare utente og
# contenitore_utenti['key'] = utente_og

# menu:
while True:
    print(red("Lista utenti: "))

    print(green("\n\n\tMENU: "))
    main_menu_choice = input(green('''

1. -
2. -
3. Effettuare BackUp o Ripristino 
4. -                                  
5. Uscire\n
'''))

    # Scelte:
    if main_menu_choice == '1':
        pass

    elif main_menu_choice == '2':
        pass

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
        pass

    elif main_menu_choice == '5':
        print(red("\nTerminazione..."))
        time.sleep(0.5)
        sys.exit()
