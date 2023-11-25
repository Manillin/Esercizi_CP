class Animale:
    x = 0
    y = 0

    def __init__(self):
        self.a = 1
        self.b = 1


class Cane(Animale):
    x = 10

    def __init__(self):
        self.a = 2


c1 = Cane()

print(c1.a)
print(c1.b)
