class Test:

    offset = 10

    @staticmethod
    def static_method(n):
        return n

    @classmethod
    def class_method(self, n):
        return n + self.offset

    def __init__(self, arg1, arg2, priv):
        self.p1 = arg1
        self.p2 = arg2 + self.offset
        self.__segreto = priv
        print("costrutture completato")

    def print_priv(self):
        print(self._Test__segreto)


print("SIM:")
a = Test("5", 3, "bohoooho")
print("@staticmethod -> ", Test.static_method("static method"))
print("@classmethod -> ", Test.class_method(10))
a.print_priv()

date_string = "22-12-2023"
l = (date_string.split('-'))

l2 = []
for i in range(len(l)):
    l2.append(int(l[i]))

print(l2)
