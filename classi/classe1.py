class persona:
    messaggio = "ciao"

    def __init__(self, arg1, arg2):
        self.nome = arg1
        self.eta = arg2

    def print_info(self):
        print("Sono " + self.nome + " e ho: " + str(self.eta) + " anni!")


il_bro = persona("Fronk", 10)
il_bro.print_info()
print(persona.messaggio)
print(il_bro.messaggio)

il_bro.messaggio = "Arrivedorci!"
print(il_bro.messaggio)
