class Test:

    offset = 10

    @staticmethod
    def static_method(n):
        return n

    @classmethod
    def class_method(self, n):
        return n + self.offset

    def __init__(self, arg1, arg2):
        print("\nInizio costruttore: ")
        self.p1 = arg1
        self.p2 = arg2 + self.offset


print("SIM:")
a = Test(5, 3)
print("@staticmethod -> ", Test.static_method("static method"))
print("@classmethod -> ", Test.class_method(10))
