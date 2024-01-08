class Casa:
    def __init__(self) -> None:
        self.__prezzo = 0

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, n):
        if n > 0:
            self.__prezzo += n
        else:
            print("Invalid price point!")


c = Casa()
print(c.prezzo)
c.prezzo = 500

print(c.prezzo)
c.prezzo = -50
