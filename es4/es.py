from functools import partial

str1 = "dfdssfdfsfdbxcfrtughwsdhsdahfgdghfjsdfva"
str2 = "sdhivadshfiasdhfkasjdhfaaksdjhalksdjfhza"
str3 = "ckvjhasdkjvhsadkjvhsdkfjhvkdjfhvsdkfjvza"

Ls = [str1, str2, str3]

freq = {}


def count_letters(freq, s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        freq[letter] = freq.get(letter, 0) + s.count(letter)


map_partial = map(partial(count_letters, freq), Ls)
list(map_partial)

print(list(freq.items()))
