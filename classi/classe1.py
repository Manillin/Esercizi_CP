class persona:
    messaggio = "ciao"

    def __init__(self, arg1, arg2):
        self.nome = arg1
        self.eta = arg2
        self.arancia = 3

    def print_info(self):
        print("Sono " + self.nome + " e ho: " + str(self.eta) + " anni!")
        print(self.arancia)


p1 = persona("Fronk", 10)
p1.print_info()
print(persona.messaggio)
print(p1.messaggio)

p1.messaggio = "Arrivedorci!"
print(p1.messaggio)
