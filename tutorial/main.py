i = 1
num = [i for i in range(i, 11)]

for numero in num:
    print(numero)

for numero in range(1, 11):
    if numero % 2:
        print("dispari")
    else:
        print("Pari")

l = list(map(lambda x: (x % 2), num))

for i in range(len(num)):
    if l[i] == 1:
        print(i, " -> pari")
    else:
        print(i, "-> dispari")
