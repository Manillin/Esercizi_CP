import datetime
import utente


class Appuntamento:

    ultimo_id = 0

    def __init__(self, nome, data: 'datetime.date') -> None:
        self.nome = nome
        self.data = data
        Appuntamento.ultimo_id += 1
        self.id = Appuntamento.ultimo_id

    def print_appuntamento(self):
        return f"{self.id})\t{self.data}: {self.nome}"


def string_to_data(string: str):
    string = string.replace(" ", "")
    componenti_data = string.split("/")
    anno = int(componenti_data[0])
    mese = int(componenti_data[1])
    giorno = int(componenti_data[2])
    data = datetime.date(anno, mese, giorno)
    return data


def inserisci_appuntamento_user(user_key, contenitore_utenti, appuntamento: 'Appuntamento'):
    utente: 'utente.Utente' = contenitore_utenti[user_key]
    utente.calendario.append(appuntamento)


def stampa_appuntamenti_per_giorno(lista_appuntamenti):
    appuntamenti_per_giorno = {}

    for appuntamento in lista_appuntamenti:
        giorno = appuntamento.data
        if giorno not in appuntamenti_per_giorno:
            appuntamenti_per_giorno[giorno] = []
        appuntamenti_per_giorno[giorno].append(appuntamento)

    for giorno, appuntamenti in appuntamenti_per_giorno.items():
        print(f"{giorno}:")
        if appuntamenti:
            for app in appuntamenti:
                print(f"  {app.nome}")
        else:
            print("Nessun appuntamento per questo giorno.")


def delete_appuntamento_by_ID_2(user: 'utente.Utente', calendario: list[Appuntamento], id):
    # Utilizza [:] per creare una copia della lista
    for appuntamento in calendario[:]:
        if appuntamento.id == id:
            calendario.remove(appuntamento)
            for user_condiviso in user.appuntamenti_condivisi:
                # Utilizza [:] per creare una copia della lista
                for app_condiviso in user_condiviso.calendario[:]:
                    if app_condiviso.id == id:
                        user_condiviso.calendario.remove(app_condiviso)
                        print(
                            f"Appuntamento eliminato anche per: {user_condiviso.nominativo}")
            return "\n\nAppuntamento Eliminato con successo!\n"
    return "Nessun appuntamento Trovato...\n"


def delete_appuntamento_by_ID(user: 'utente.Utente', calendario: list[Appuntamento], id):
    appuntamento_trovato = False
    calendario_copy = calendario.copy()  # Crea una copia della lista

    for appuntamento in calendario_copy:
        if appuntamento.id == id:
            calendario.remove(appuntamento)
            appuntamento_trovato = True

    if appuntamento_trovato:
        for user_condiviso in user.appuntamenti_condivisi:
            user_condiviso_copy = user_condiviso.calendario.copy()  # Crea una copia della lista
            for app_condiviso in user_condiviso_copy:
                if app_condiviso.id == id:
                    user_condiviso.calendario.remove(app_condiviso)
                    print(
                        f"Appuntamento eliminato anche per: {user_condiviso.nominativo}")
        return "Appuntamento Eliminato!\n"
    else:
        return "Nessun appuntamento Trovato...\n"
