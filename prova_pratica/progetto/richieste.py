import users
from colorama import Fore, Style


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def verde(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


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


def richieste_subordinati(selected_user, contenitore_utenti):
    if isinstance(selected_user, users.Responsabile):
        lista_richieste = []
        for subordinato in selected_user.lista_subordinati:
            for r in range(len(contenitore_utenti[subordinato].get_richieste())):
                lista_richieste.append(
                    [contenitore_utenti[subordinato].richieste_pag[r], subordinato])

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
        print(verde(f"Debug: <<Richieste per utente {sub_key}"))
        print(contenitore_utenti[sub_key].get_richieste)
    else:
        print(red("Missing auth to modify requests"))


# Istruzioni in caso lanciato come script
if __name__ == "__main__":
    pass
