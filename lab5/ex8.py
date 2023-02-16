import re
with open("row.txt") as myfile:
    for line in myfile:
        ans=""
        res=re.split(r"[A-Z]", line)
        for i in res:
            if i!='':
                ans+=i
        print(ans)