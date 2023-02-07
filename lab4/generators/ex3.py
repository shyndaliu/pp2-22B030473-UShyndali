def iterr(max):
    x=0
    while(x<=max):
        yield x
        x+=12


n=int(input())
for i in iterr(n):
    print(i)