def solve(numheads, numlegs):
    rab=numlegs/2-numheads
    chick=numheads-rab
    return [int(rab), int(chick)]

print(solve(35,94))
