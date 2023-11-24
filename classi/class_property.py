class House:
    def __init__(self, num):
        self.__price = int(num)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, np):
        new_price = int(np)
        if new_price < self.__price:
            print("Invalid price...")
        else:
            self.__price = new_price


casa1 = House(2000)
print(casa1.price)
casa1.price = 5000
print(casa1.price)
casa1.price = 200
