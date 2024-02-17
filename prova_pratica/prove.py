data_input = "20     22/    12/21    "
data_input = data_input.replace(" ", "")

# Dividi la stringa in base al carattere "/"
componenti_data = data_input.split("/")

# Converte i componenti in interi
anno = int(componenti_data[0])
mese = int(componenti_data[1])
giorno = int(componenti_data[2])

print("Anno:", anno)
print("Mese:", mese)
print("Giorno:", giorno)
