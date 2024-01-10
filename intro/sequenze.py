import time


def timerFunction(f):
    def func(arg):
        print("Added func")
        f(arg)
        print("Func terminated!")
    return func


@timerFunction
def print_nome(a):
    for i in range(a):
        print(i)
    return


print_nome(5)
