# lambda con filter
i = 1
nums = [i for i in range(i, 11)]
disp = filter(lambda x: (x % 2 != 0), nums)
dispL = list(disp)
print(dispL)

# lambda com map
map = map(lambda x: -x, nums)
mapL = list(map)
print(mapL)
