class dec:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Invocato")
        self.f()

    def call(self):
        self.f


@dec
def foo():
    print("Function call! ")


foo()
