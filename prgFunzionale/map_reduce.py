from functools import *

interi = [1, 2, 3, 4, 5]
int = [i for i in range(1, 6)]


def somma(x, y):
    return x+y

# sommapart = partial(somma, y=10)
# red = reduce(somma, int)
# print(red)


# creazione di un set da una lista:

s_reduce = reduce(lambda x, y: x.union(set([y])), [1, 2, 3, 4], set())
# spiegazione:
'''
la funzione reduce ha 3 parametri in questo caso:
1. la funzione lambda
2. una lista (iterabile)
3. una funzione da chiamare sul primo elemento dell'iterabile

alla prima chiamata viene invocata set() sul primo elemento della lista 
che risulta nel set -> {1}. questo sarà la x per la prossima chiamata.
In quanto set possiamo usare la primitiva .union() e trasformiamo in set 
la y che presa da parte sarebbe un intero, quindi  set([y]) trasforma l'int
in una lista di lunghezza 1 con l'intero in questione.
A questo punto avremo {1}.union(set([2])) che risulta in {1,2}.
procedendo con la stessa logica arriveremò all'ultima iterazione, che 
tradotta risulta in: {1,2,3}.union(set([4])) -> {1,2,3,4}
fine spiegazione
'''


'''a = [5]
s_ = set(a)
print(s_)'''
print(s_reduce)
