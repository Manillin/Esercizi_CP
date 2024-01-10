class House:
    def __init__(self, str='') -> None:
        self.__price = 0
        self.paese = str

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, n):
        if n > 0:
            self.__price = n
        else:
            print(f"Invalid price for house item in {self.paese}")
        return


c1 = House('Maldive')
c2 = House('Caraibi')

c1.price = 50
c2.price = -5

print(c1.price)
