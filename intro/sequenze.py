#Scrivere un programma che prenda in input un testo lungo.
#Stampi la frequenza di ogni carattere.
#Plus: stampare le frequenze in ordine crescente


testo = input("inserisci testo: ")
freq = {}

for _ in testo:
    if _ not in freq:
        freq[_] = 1
    else:
        freq[_] +=1


l = sorted(freq.items(), key=lambda x:x[1])
new_dict = dict(l)
# list = [('a',1),('b',9),('c',3),('d',2)]
for k,v in new_dict.items():
    print(f'{k}: {v}')