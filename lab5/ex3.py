import re
with open("row.txt") as myfile:
    for line in myfile:
        res=re.findall(r"[a-z]{1,}[_]{1,}[a-z]{1,}",line)
        if(len(res)!=0):
            for i in res:
                print(i)