import math
def isp(i):
    for j in range(2,i-1):
        if(i%j==0):
            return False
    return True

n=int(input())
a=list(range(1,n+1))
a=list(filter(lambda x: isp(x), a))
print(a)