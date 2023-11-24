
class Automobile():
    def __init__(self):
        self.posizione = 0

    def move(self, l):
        self.posizione += l


class Barca():
    def affonda(self):
        self.affondato = True

    def muoviti(self, l):
        if self.affondato:
            return "Affondato...\n"
        else:
            print("Moving...")


class Anfibio(Automobile, Barca):
    # esplicitare tutti i costruttori da usare:
    def __init__(self):
        Automobile.__init__(self)
        Barca.__init__(self)
        super.__init__(self)


a = Anfibio()
print(Anfibio.__mro__)
# Cambio ordine classi base (classi madre)
Anfibio.__bases__ = (Barca, Automobile)
print("\n", Anfibio.__mro__)
