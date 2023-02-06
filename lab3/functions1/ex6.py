def reverser(s):
    a=s.split()
    a.reverse()
    ans=""
    for i in a:
        ans+=i+" "
    return ans

print(reverser("i love programming<3"))