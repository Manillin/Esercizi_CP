from functools import partial

str1 = "asdgfgdhddwg"
str2 = "sdsfdjgsodgjsod"
str3 = "dfsojjdfsjfdfdsoj"

Ls = [str1, str2, str3]

# Dizionario delle frequenze
freq = {}

# Funzione per contare le lettere in una stringa e aggiornare il dizionario delle frequenze


def count_letters(freq, s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        freq[letter] = freq.get(letter, 0) + s.count(letter)


# Utilizza map con functools.partial per fornire il dizionario
map_partial = map(partial(count_letters, freq), Ls)

# Consuma il risultato di map
list(map_partial)

# Stampa il dizionario delle frequenze
print(freq)
