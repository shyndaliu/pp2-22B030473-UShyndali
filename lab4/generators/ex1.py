def iterr(max):
    x=1
    while x<=max:
        yield x*x
        x+=1


n=int(input())
for x in iterr(n):
    print(x)