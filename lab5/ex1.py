import re
with open("row.txt","r", encoding='utf-8') as myfile:
    for line in myfile:
        res=re.findall(r"a[b]{0,}", line)
        if(len(res)!=0):
            for i in res:
                print(i)