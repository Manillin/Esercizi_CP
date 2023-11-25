class Animale:
    x = 0
    y = 0

    def __init__(self):
        self.a = 1
        self.b = 10


class Cane(Animale):
    x = 10

    def __call__(self):
        print("Cane invocato")

    def __init__(self):
        # super().__init__()
        self.a = 2

    def woof(self):
        self.x = "woof!"
        print(x)


c1 = Cane()

print(c1.a)
# print(c1.b) # funziona solo se nel costruttore ho: super().__init__()
c1()
