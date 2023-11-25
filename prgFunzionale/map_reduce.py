from functools import reduce

i = 1
nums = [i for i in range(i, 5)]
print(nums)

red = reduce(lambda x, y: x+y, nums)
print(red)

setr = reduce(lambda x, y: x.union(set([y])), nums, set())
print(setr)
