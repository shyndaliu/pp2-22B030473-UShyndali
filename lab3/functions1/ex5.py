from itertools import permutations
def func(s):
    a=[''.join(i) for i in permutations(s)]
    return a

print(func("abc"))
