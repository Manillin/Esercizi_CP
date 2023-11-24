def funzione(n):
    return (n*n)+1


numbers = [1, 2, 3, 4]

insta_set = list(map(funzione, numbers))
insta_set2 = set(map(lambda x: (x*x)+1, numbers))

print(insta_set)
print(insta_set2)
