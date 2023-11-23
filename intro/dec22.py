def decoratore(fun):
    def funplus(*args,**kwargs):
        res = fun(*args,**kwargs)
        print(f'Risultato {res}')
        return res
    return funplus

@decoratore
def square(x):
    return x**2

a = 5
square(a)