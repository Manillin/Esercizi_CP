import sys


args = sys.argv
print("Arrrrgh: ", args)

for i in range(len(args[0])):
    print(i)

for item in args:
    print(item)
