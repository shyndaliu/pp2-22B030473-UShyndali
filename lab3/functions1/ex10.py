def uniq(*num):
    a={}
    for i in num:
        if a.get(i) is not None:
            continue
        else:
            a[i]=True
    print(*a.keys())

uniq(1,1,2,5,8,9,4,4,5)