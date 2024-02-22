
class Farmaco:
    def __init__(self, nominativo, frequenza) -> None:
        self.nominativo = nominativo
        self.frequenza = frequenza


if __name__ == '__main__':
    import argparse
    import paziente
    import sys

    def write_terapia_giorni_successivi_to_file(paziente: 'paziente.Paziente', giorni, dest_file):
        print("Invoked")
        with open(dest_file, 'w') as file:
            for g in range(giorni):
                file.write((f"Giorno: {g+1}\n"))
                for farmac in paziente.lista_farmaci:
                    if (g+1) % farmac.frequenza == 0:
                        file.write((farmac.nominativo + '\n'))
                file.write('\n')
        print("Success!\n")

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', help='Nome del file di backup')
    parser.add_argument('file_destinazione',
                        help='Nome del file su cui esportare')
    parser.add_argument(
        'key_paziente', help='key paziente (nominativo senza spazi)')
    parser.add_argument('giorni', help='numero giorni terapia')

    args = parser.parse_args()
    file_backup = args.file_name
    dest_file = args.file_destinazione
    paz = args.key_paziente
    giorni = int(args.giorni)

    contenitore_pazienti = paziente.load_backup_pazienti(file_backup)
    if paz in contenitore_pazienti:
        paziente_attuale = contenitore_pazienti[paz]
    else:
        print("ERRORE")
        sys.exit()

    write_terapia_giorni_successivi_to_file(
        paziente_attuale, giorni, dest_file)
