l = ['ciao', 'ao', 'hola', 'ciao']

filter_ciao = filter(lambda x: x == 'ciao', l)
print(list(filter_ciao))


append123 = map(lambda x: x+'123', l)
print(list(append123))
