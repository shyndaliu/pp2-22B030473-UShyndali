def backw(max):
    x=max
    while x>=0:
        yield x
        x-=1

n=int(input())
for i in backw(n):
    print(i)