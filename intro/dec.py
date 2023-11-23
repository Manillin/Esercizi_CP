def uppercase(function):
    def wrapper():
        stringa = function()
        print(stringa.upper())
        return stringa
    return wrapper 

@uppercase
def saluta():
    return "ciaooooo"

saluta()


