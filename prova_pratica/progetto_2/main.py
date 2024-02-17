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
        print("Y")
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


def string_to_data(string: str):
    string = string.replace(" ", "")
    componenti_data = string.split("/")
    anno = int(componenti_data[0])
    mese = int(componenti_data[1])
    giorno = int(componenti_data[2])
    data = datetime.date(anno, mese, giorno)
    return data


# MENU

contenitore_utenti = {}
ceo = users.Utente('User 1', [], 5)
# Format Contenitore Utenti:
# USER_KEY(nospazi) : USER('nominativo', 'lista', 'saldo')
contenitore_utenti['user1'] = ceo

if __name__ == '__main__':
    while True:
        print(red("\nLista Utenti: "))
        for pre_user in contenitore_utenti.values():
            print(green(pre_user.nominativo))

        print(green("\n\n\tMENU: "))
        main_menu_choice = input(green('''

1. Creazione Nuovo Utente
2. Log In Utente
3. Effettuare BackUp o Ripristino 
4. Esportare le transazioni in formato testuale                                   
5. Uscire

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
            menu_ripristino = '''\n
1. Effettuare un BackUp degli utenti attuali 
2. Ripristinare stato da un precedente backup
3. Tornare al menu principale\n

'''
            print(green(menu_ripristino))
            nome_file = 'backup.pkl'
            backup_choice = input(": ")
            if backup_choice == '1':  # fare backup
                crea_backup_utenti(nome_file, contenitore_utenti)
                continue
            elif backup_choice == '2':  # ripristinare da backup
                contenitore_utenti = load_backup_utenti(nome_file)
                continue
            elif backup_choice == '3':
                continue
            else:
                print(red("\nInvalid choice, torno al menu principale"))
                continue

        elif main_menu_choice == '4':
            nome_file_testuale = 'transazioni.txt'
            # contiene
            lista_transazioni_esportazione = []
            for utente in contenitore_utenti.values():
                for transazione_utente in utente.lista_transazioni:
                    lista_transazioni_esportazione.append(transazione_utente)
            counter = 1
            with open(nome_file_testuale, 'w') as f:
                for tran in lista_transazioni_esportazione:
                    f.write(f"{counter}. {tran.print_transazione()}\n")
                    counter += 1
            print(
                green(f"Transazioni esportate con successo in {nome_file_testuale}"))
            continue

        elif main_menu_choice == '5':
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
            if user.saldo < 0:
                print(
                    green(f"\n\nBentornato {user.nominativo}, Il tuo saldo attuale è: "), end='')
                print(red(f"{user.saldo}€ "))
                print(green("Cosa vuoi fare? \n\n"))
            else:
                print(
                    green(f"\n\nBentornato {user.nominativo}, Il tuo saldo attuale è: {user.saldo}€ \nCosa vuoi fare? \n\n"))
            user_choice = input(green(
                f"1. Nuovo Versamento\n2. Nuovo Prelievo\n3. Vedere lo storico delle operazioni\n4. Esportare storico delle operazioni\n5. Tornare al Menu Principale\n"))

            # possibile scelte:
            if user_choice == '1':
                print(green(f"\n\t<< Nuovo Versamento: >>\n"))
                versamento = int(
                    input(green("Quanto vuoi versare sul conto: ")))
                if versamento <= 0:
                    print(red("Non puoi fare versamenti negativi..."))
                    continue

                scelta_data = input(green(
                    f"Scegli la data della transazione [ YYYY/MM/DD ] o premi enter per selezionare la data odierna: \n"))
                if scelta_data:
                    try:
                        scelta_data = scelta_data.replace(" ", "")
                        componenti_data = scelta_data.split("/")
                        anno = int(componenti_data[0])
                        mese = int(componenti_data[1])
                        giorno = int(componenti_data[2])
                        data_transazione = datetime.date(anno, mese, giorno)
                    except:
                        print(red("Formato della data errato! [ YYYY/MM/DD ]"))
                        continue
                else:
                    data_transazione = datetime.date.today()

                versamento_singolo = transazione.Transazione(
                    data_transazione, versamento, 'versamento')
                user.lista_transazioni.append(versamento_singolo)
                user.saldo += versamento

            elif user_choice == '2':
                print(green(f"\n\t<< Nuovo Prelievo: >>\n"))
                prelievo = abs(
                    int(input(green("Quanto vuoi prelevare dal conto: "))))
                data_prelievo = datetime.date.today()
                prelievo_singolo = transazione.Transazione(
                    data_prelievo, prelievo, 'prelievo')
                saldo_corrente = user.saldo - prelievo
                if saldo_corrente <= 0:
                    print(
                        red(f"Attenzione il tuo saldo attuale risulta negativo: {saldo_corrente}€"))
                else:
                    print(green("Prelievo avvento con successo"))
                user.lista_transazioni.append(prelievo_singolo)
                user.saldo = saldo_corrente

            # Vedere lo storico delle operazioni
            elif user_choice == '3':
                scelta_storico = input(
                    f"\n1. Vedere lo storico intero (comportamento default)\n2. Vedere lo storico filtrato per data\n")
                if scelta_storico == '1' or not scelta_storico:
                    print("\n\nLista di tutte le transazioni registrate: ")
                    if user.lista_transazioni == []:
                        print(red("\nNon sono presenti transazioni a tuo nome! \n"))
                        continue
                    for tran in user.lista_transazioni:
                        print(green(f"{tran.print_transazione()}"), end='\n')

                elif scelta_storico == '2':
                    try:
                        print(green("\nFormato data -> [ YYYY/MM/DD ]"))
                        stringa_data_inizio = input("Data Inizio: ")
                        stringa_data_fine = input("Data Fine: ")
                        data_inizio = string_to_data(stringa_data_inizio)
                        data_fine = string_to_data(stringa_data_fine)
                        lista_transazioni_filtrate = transazione.filtra_data(
                            user.lista_transazioni, data_inizio, data_fine)
                        print(
                            green(f"\n\nTransazioni registrate da {data_inizio} <-- a --> {data_fine}"))
                        for transazione_filtrata in lista_transazioni_filtrate:
                            print(
                                green(transazione_filtrata.print_transazione()), end='\n')
                        print("\n\n")
                    except:
                        print(
                            red("Formato data sbagliatoo! [ YYYY / MM / DD ]"))
                        continue
                else:
                    print(red("\nScelta invalida...\n"))
                    continue

            elif user_choice == '4':
                try:
                    counter = 0
                    with open('transazioni_utente.txt', 'w') as file:
                        for transac in user.lista_transazioni:
                            file.write(
                                f"{counter}. {transac.print_transazione()}\n")
                            counter += 1
                    print("Esportazione riuscita in: transazioni_utente.txt !\n\n")
                except:
                    print(red("Esportazione fallita... \nTermino Programma"))
                    time.sleep(1)
                    sys.exit()

            elif user_choice == '5':
                print(green("\nReturning to main menu: "))
                stay_on_second_menu = True

            else:
                print(red("Scelta invalida "))
                continue
