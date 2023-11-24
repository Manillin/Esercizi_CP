def calculateSquare(n):
    return n*n


def testL(n):
    return (n*n)+1


numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = list(result)
print(numbersSquare)

instaset = set(map(lambda x: x+2, numbers))
instaset2 = list(map(testL, numbers))
print("Lambda: ", instaset)
print("Manuale: ", instaset2)
