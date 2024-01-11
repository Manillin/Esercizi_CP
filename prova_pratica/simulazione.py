import time


class Utente:
    def __init__(self, identificativo, stipendio, orario, ruolo) -> None:
        self.identificativo = identificativo
        self.stipendio = stipendio
        self.orario = orario
        self.ruolo = ruolo
        self.richieste = []
        self.listaSub = []

    def richiesta_pagamento(self):
        print(f"Ciao {self.identificativo}, cosa vuoi fare? ")
        valid_choice = False
        while not valid_choice:
            choice = input(
                "Fare nuova richiesta di pagamento (1) | Visualizzare cronologia richieste (2):  ")
            if choice != '1' and choice != '2':
                print("Scelta non valida! riprova")
                continue

            if choice == '1':
                # logica incrementale di ID per ogni nuova richiesta
                stato_richiesta = 'pending'
                id_richiesta = len(self.richieste)
                ore_richiesta = int(input("Ore totali della richiesta: "))
                self.richieste.append(
                    [id_richiesta, ore_richiesta, stato_richiesta])
                valid_choice = True

            else:
                print("\nRichieste precedenti: ")
                for richiesta in self.richieste:
                    print(richiesta)
                valid_choice = True

    def get_richieste(self):
        return self.richieste

    def visualizza_richieste_subordinato(self):
        lista_richieste_subordinati = []
        for subordinato in self.listaSub:
            for r in range(len(utenti[subordinato].get_richieste())):
                lista_richieste_subordinati.append(
                    [utenti[subordinato].richieste[r], subordinato])
        for richiesta in lista_richieste_subordinati:
            print(richiesta)

    def get_index(self, n):
        for index in range(len(self.richieste)):
            req = self.richieste[index]
            if req[0] == int(n):
                return index
        return "Error"

    def modifica_richiesta(self, index, choice, sub_key):
        target = utenti[sub_key].richieste[index]
        if choice == 'a':
            target[2] = 'approved'
        else:
            target[2] = 'rejected'
        print(f"Richieste per utente {sub_key}")
        print(utenti[sub_key].richieste)

    # format richiesta -> [ id, int(ore) , 'status']
    def get_ore_e_importo_totale(self):
        lista_importi = []
        ore_totali = 0
        for richiesta in self.richieste:
            if richiesta[2] == 'approved':
                lista_importi.append(richiesta)
                ore_totali += richiesta[1]
        return lista_importi, ore_totali


# main
utenti = {}
# Creazione CEO e inserimento nel sistema
user_zero = Utente("Fronk Von", 4000, 40, 'r')
utenti[user_zero.identificativo.strip().lower().replace(" ", "")] = user_zero
print(utenti.items())


valid_user = False
user = ''
while not valid_user:
    job = input("Creazione Utente (c) | Log in (l) ")
    if job == 'c':
        user_name = input("Inserisci nome e cognome: ")
        id_user = user_name.strip().lower().replace(" ", "")
        if id_user in utenti:
            print("Utente già registrato, procedi con il log in!\n\n")
            continue
        stipendio = int(input("inserisci il tuo stipendio: "))
        orario = input("Inserisci il tuo orario: ")
        # controllo ruolo ed esistenza responsabile se utente subordiato
        role = input(
            "Inserisci il tuo ruolo [ s -> subordinato | r -> responabile]: ").lower()
        if role != 's' and role != 'r':
            print("Ruolo non riconosciuto...\n\n")
            continue
        if role == 's':
            resp = input("Nome del tuo responsabile: ").strip(
                "").lower().replace(" ", "")
            if resp not in utenti:
                print("Responsabile inesistente, controlla le informazioni!\n\n")
                continue

        # Creazione utente andata a buon fine, inseriento nel sistema:
        utenti[id_user] = Utente(user_name, stipendio, orario, role)
        # aggiunta subordinato alla lista del relativo responsabile
        try:
            utenti[resp].listaSub.append(id_user)
        except:
            print("Aggiunta subordinato al responsabile fallita\n")

        valid_user = True
    else:
        id_user = input("Inserisci il tuo identificativo: ").strip(
        ).lower().replace(" ", "")
        if id_user not in utenti:
            print("Utente non riconosciuto, procedi con la creazione!\n\n\n")
            continue
        valid_user = True

user = utenti[id_user]
print(f"\nUtente Selezionato << {user.identificativo} >>\n\n")

# Scelta in caso utente subordinato
if user.ruolo == 's':
    user_choice = input(
        "Vuoi fare nuova richiesta di pagamento (n) | Visualizzare resoconto (v)").lower()
    if user_choice == 'n':
        user.richiesta_pagamento()
        user.richiesta_pagamento()
    elif user_choice == 'v':
        print("Visualizzazione del resoconto: ")
        lista_importi, ore_totali = user.get_ore_e_importo_totale()
        for importo in lista_importi:
            print(importo)
        print(f"Ore totali: {ore_totali}")
    else:
        print("Invalid choice!")


# cambio user per test:
user = utenti['fronkvon']
print(f"\nUtente Selezionato << {user.identificativo} >>\n\n")
print(user.listaSub)
if user.ruolo == 'r':
    while True:
        print("Richieste dei subordinati: ")
        user.visualizza_richieste_subordinato()
        change_richieste = input(
            "Vuoi approvare o rifiutare nuove richieste?: (Y) or (N): ").lower()
        if change_richieste == 'y':
            resp_choice = input("Approvare (a) o Rifiutare (r): ")
            sub = input("Per quale subordinato?: ")
            id_richiesta = input("ID della richiesta: ")  # 0
            index = utenti[sub].get_index(id_richiesta)
            user.modifica_richiesta(index, resp_choice, sub)

        else:
            print("Esco da dashboard manager\n")
            time.sleep(1)
            break

cambio = input("Log in nuovo utente: ").strip().lower().replace(" ", "")
user = utenti[cambio]

print(
    f"\nBentornato << {user.identificativo} >> | Ruolo: {user.ruolo} | Stipendio: {user.stipendio}")
# Scelta in caso utente subordinato
if user.ruolo == 's':
    user_choice = input(
        "Vuoi fare nuova richiesta di pagamento (n) | Visualizzare resoconto (v)").lower()
    if user_choice == 'n':
        user.richiesta_pagamento()
        user.richiesta_pagamento()
    elif user_choice == 'v':
        print("Visualizzazione del resoconto: ")
        lista_importi, ore_totali = user.get_ore_e_importo_totale()
        for importo in lista_importi:
            print(importo)
        print(f"Ore totali: {ore_totali}")
    else:
        print("Invalid choice!")
