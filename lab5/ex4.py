import re
with open("row.txt") as myfile:
    for line in myfile:
        res=re.findall(r"[A-Z]{1,}[a-z]{1,}",line)
        if(len(res)!=0):
            for i in res:
                print(i)