class Persona:
    def __init__(self, nome, eta=0):
        self.nome = nome
        self.eta = eta
        self.yop = 1

    def __getattrbute__(self, campo):
        if campo == 'eta':
            raise AttributeError("non si chiede l'eta!!")
        else:
            return super().__getattribute__(campo)


p1 = Persona('fronk', 23)
p2 = Persona('pesca', 20)


print(p2.nome)
print(p2.eta)
