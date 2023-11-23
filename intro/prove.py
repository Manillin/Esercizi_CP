#Rubrica 

rubrica = {
    }

while True:
    risp = input("1.Add\n2.View all\n3.Delete\n4.Delete all\n\n")
    if risp == '1':
        nome = input("nome: ")
        tel = input("telefono: ")
        if nome in rubrica:
            print("Nome già presente! Inserimento illegale\n")
        else:
            rubrica[nome] = tel
            print("\nContatto aggiunto!\n")
    elif risp == '2':
        for key,value in rubrica.items():
            print(f'{key}: {value}')
        print("\n\n")
    elif risp == '3':
        canc = input("Nome da eliminare: ")
        if canc in rubrica:
            del rubrica[canc]
        else:
            print("Nome non presente nella rubrica... fallback ...")
    elif risp == '4':
        rubrica.clear()
        print("dizionario wiped\n")
    else:
        print("operazione non definita...\nRange -> [1-3]")