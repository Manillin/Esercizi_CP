import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('echo')
# args = parser.parse_args()
# print(args.echo)

# Specificare il nome del file da cui fare backup
# Specificare il nome dell'utente le cui richieste sono da esportare

parser = argparse.ArgumentParser()
parser.add_argument(
    'file_backup', help='Nome del file da cui effettuare il backup', type=str)
parser.add_argument(
    'user', help='Specifica User (nominativo senza spazi) le cui richieste vanno esportate'
)
args = parser.parse_args()
print(args.file_backup)
print(args.user)
