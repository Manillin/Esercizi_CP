from colorama import Fore, Style


def red(x): return f"{Fore.RED}{x}{Style.RESET_ALL}"
def green(x): return f"{Fore.GREEN}{x}{Style.RESET_ALL}"


print(
    green(f"Inserisci i farmaci che desideri: [Premi enter quando hai finito]"))
farmaci = "."
lista_farmaci = []
while farmaci:
    farmaci = input(": ")
    lista_farmaci.append(farmaci)

for farm in lista_farmaci:
    print(farm)
