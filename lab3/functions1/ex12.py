def histogram(*val):
    s=""
    for i in val:
        for j in range(i):
            s+="*"
        print(s)
        s=""

histogram(1,3,2,4,7)