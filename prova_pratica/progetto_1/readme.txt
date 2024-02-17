Struttura Progetto e Assunzioni fatte per il completamento nel limite di 2h:


Struttura:
Tutti gli utenti e le loro richieste sono salvati in un dizionario:
    - contenitore_utenti = {}
    - KEY: USER
    - key  = nominativo senza spazi e in minuscolo 
    - user = istanza di un oggetto classe User

Per il log in:
    - Utente può inserire nominativo con o senza spazi e verrà comunque riconosciuto 
    - Una volta fatto il log in potrà fare le varie operazioni


Assunzioni:
stipendio -> intero che rappresenta lp stipendio annuale di un utente 
ore -> rappresenta le ore settimanali di un utente
ruolo -> subordinato o responsabile


File:
main.py -> esegue il programma intero e la sua logica
richieste.py -> gestisce le funzioni per manipolare le richieste di pagamento
users.py -> gestisce utenti, gerarchicamente: Responsabile e Subordinato

Controlli:
Sono stati fatti vari controlli, quali:
    - Esistenza di un responsabile per un subordinato 
    - Controllo esistenza utenti per il log in 
    - Vari controlli in input

NON sono stati fatti tutti i possibili controlli (limite di 2h), quali:
    - Quando si crea un utente se non si specifica lo stipendio il programma crasha 
    - Importazione di file sbagliati e non presenti nella directory
    









