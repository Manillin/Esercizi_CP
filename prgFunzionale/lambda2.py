iter = [i for i in range(11)]
print(iter)

f_items = filter(lambda x: x % 2, iter)
# spiegazione:
'''
filter ha il compito di selezionare item in base al loro valore di ritorno una 
volta che gli si applica la funzione definita.
in questo caso, i numeri dispari se messi in modulo con 2 fanno 1, che risulta 
True, e quindi il risultato verrà messo in f_items.
Mentre i dispari facendo %2 -> 0, risulteranno false [0 == False | 1 == True]
'''

f_list = list(f_items)
print(f_list)


stringhe = ["ciao", "come", "stai", "cocco"]


def string_filter(str):
    if 'c' in str:
        return True
    return False


str_filter = filter(string_filter, stringhe)
str_filter2 = filter(lambda x: 'a' in x, stringhe)
list_str = list(str_filter)

print(list_str)
print("sec: ")
print(list(str_filter2))
