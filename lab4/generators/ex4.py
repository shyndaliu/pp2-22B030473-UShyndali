def squares(start, end):
    x=start
    while x<=end:
        yield x*x
        x+=1

a=int(input())
b=int(input())
for i in squares(a, b):
    print(i)