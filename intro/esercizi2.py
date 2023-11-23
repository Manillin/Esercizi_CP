valori = []
while True:
    try:
        value = int(input("Inserisci un numero: "))
    except ValueError:
        print("Non hai inserito un numero...")
        break
    valori.append(int(value))
 
l = map(lambda x:x+1,valori)
for _ in l:
    print(_)
