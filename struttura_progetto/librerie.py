import sys

# print(sys.path)


def mangiare():
    print("Mangio")


def nome():
    return f"my name {__name__}"


if __name__ == '__main__':
    print("nome interno - chiamata locale")
    nome()
