
class Cane:
    numero_cani = 0

    @classmethod
    def get_instance_number(cls):
        return cls.numero_cani

    def __init__(self, sx, zampe=4, coda=True, age=0, malato=False, spavaldo=False):
        self.zampe = 4
        self.coda = True
        self.age = 0
        self.sx = sx
        self.__malato = malato
        self.__spavaldo = spavaldo
        Cane.numero_cani += 1

    @property
    def malato(self):
        if self.spavaldo:
            return False
        else:
            return self.__malato

    @malato.setter
    def malato(self, m):
        self.__malato = m

    @property
    def spavaldo(self):
        return self.__spavaldo

    @spavaldo.setter
    def spavaldo(self, s):
        self.__spavaldo = s

    def abbaia(self):
        pass

    def cammina(self):
        pass

    def corri(self):
        pass


c1 = Cane('m')
c2 = Cane('m')
c3 = Cane('f')


print(Cane.get_instance_number())
