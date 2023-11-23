testo = input("testo: ")

letters = []
freq = []

for char in testo:
    if char in letters:
        freq[letters.index(char)] += 1
    else:
        letters.append(char)
        freq.append(1)

print(letters)
print(freq)



print("Ordinamento: ")

i=0
while (i <= len(freq)):
    index = freq.index(max(freq))
    print(letters[index], " -> ", freq[index])
    del(freq[index])
    del(letters[index])
    i+=1

    