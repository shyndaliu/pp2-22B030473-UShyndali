import re
with open("row.txt") as myfile:
    for line in myfile:
        res=re.findall(r"a[^ ]{0,}b",line)
        if(len(res)!=0):
            for i in res:
                print(i)