def Even(max):
    x=0
    while x<=max:
        yield x
        x+=2

n=int(input())
ans=[]
for i in Even(n):
    ans.append(i)
print(ans, sep=", ")